/**
 * Gardablick — i18n + Cookie Consent
 * Client-side translation system matching the Next.js LanguageContext,
 * plus cookie consent modal matching CookieConsent.tsx.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "gardablick-locale";
  var COOKIE_CONSENT_KEY = "gardablick-cookie-consent";
  var API_BASE = "/api";
  var translations = {};
  var currentLocale = "it";

  /* ========== TRANSLATION ENGINE ========== */

  /**
   * Resolve a dot-separated key path (e.g. "cookie.title") from the
   * translations JSON object.
   */
  function resolveKey(obj, path) {
    var keys = path.split(".");
    var current = obj;
    for (var i = 0; i < keys.length; i++) {
      if (current && typeof current === "object" && keys[i] in current) {
        current = current[keys[i]];
      } else {
        return path; // fallback: return the key itself
      }
    }
    return typeof current === "string" ? current : path;
  }

  /** Translate a single key */
  function t(key) {
    return resolveKey(translations, key);
  }

  /** Apply translations to all elements with [data-i18n] */
  function applyTranslations() {
    var elements = document.querySelectorAll("[data-i18n]");
    for (var i = 0; i < elements.length; i++) {
      var key = elements[i].getAttribute("data-i18n");
      var translated = t(key);
      if (translated !== key) {
        elements[i].textContent = translated;
      }
    }
    // Also apply to elements with data-i18n-placeholder (for form inputs)
    var placeholders = document.querySelectorAll("[data-i18n-placeholder]");
    for (var j = 0; j < placeholders.length; j++) {
      var pKey = placeholders[j].getAttribute("data-i18n-placeholder");
      var pVal = t(pKey);
      if (pVal !== pKey) {
        placeholders[j].setAttribute("placeholder", pVal);
      }
    }
  }

  /** Fetch translations from the API */
  function fetchTranslations(locale, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", API_BASE + "/translations/" + locale + "/");
    xhr.onload = function () {
      if (xhr.status === 200) {
        try {
          translations = JSON.parse(xhr.responseText);
        } catch (e) {
          translations = {};
        }
      }
      if (callback) callback();
    };
    xhr.onerror = function () {
      if (callback) callback();
    };
    xhr.send();
  }

  /** Update the active language indicator in header */
  function updateLangIndicators() {
    var allLangs = document.querySelectorAll("[data-lang]");
    for (var i = 0; i < allLangs.length; i++) {
      var lang = allLangs[i].getAttribute("data-lang");
      var isMobile = allLangs[i].closest("#mobile-menu") !== null;

      if (lang === currentLocale) {
        if (isMobile) {
          allLangs[i].className = "text-[#02033b] uppercase text-[18px] font-medium cursor-pointer";
        } else {
          // Desktop: active state. The actual color (white vs navy) is handled
          // by the scrolled state CSS; we just toggle the font weight class.
          allLangs[i].classList.remove("font-extralight");
          allLangs[i].classList.add("font-medium");
          allLangs[i].style.opacity = "";
        }
      } else {
        if (isMobile) {
          allLangs[i].className = "text-[#02033b]/70 uppercase text-[18px] font-extralight cursor-pointer hover:opacity-80";
        } else {
          allLangs[i].classList.remove("font-medium");
          allLangs[i].classList.add("font-extralight");
        }
      }
    }
  }

  /** Set locale: save to localStorage + cookie, fetch translations */
  function setLocale(locale) {
    currentLocale = locale;
    try {
      localStorage.setItem(STORAGE_KEY, locale);
    } catch (e) { /* private browsing */ }
    document.cookie = "locale=" + locale + ";path=/;max-age=31536000";
    document.documentElement.setAttribute("lang", locale);

    fetchTranslations(locale, function () {
      applyTranslations();
      updateLangIndicators();
    });
  }

  /** Initialize locale from storage */
  function initLocale() {
    var saved = null;
    try {
      saved = localStorage.getItem(STORAGE_KEY);
    } catch (e) { /* private browsing */ }
    currentLocale = saved && (saved === "it" || saved === "en" || saved === "de") ? saved : "it";
    document.cookie = "locale=" + currentLocale + ";path=/;max-age=31536000";
    document.documentElement.setAttribute("lang", currentLocale);

    fetchTranslations(currentLocale, function () {
      applyTranslations();
      updateLangIndicators();
    });
  }

  /* ========== LANGUAGE SWITCHER CLICK HANDLERS ========== */

  function initLanguageSwitcher() {
    var allLangs = document.querySelectorAll("[data-lang]");
    for (var i = 0; i < allLangs.length; i++) {
      (function (el) {
        el.addEventListener("click", function () {
          var lang = el.getAttribute("data-lang");
          if (lang && lang !== currentLocale) {
            setLocale(lang);

            // If in mobile menu, close it
            var mobileMenu = document.getElementById("mobile-menu");
            var menuBtn = document.getElementById("mobile-menu-btn");
            if (mobileMenu && el.closest("#mobile-menu")) {
              mobileMenu.classList.add("translate-x-full");
              mobileMenu.classList.remove("translate-x-0");
              document.body.style.overflow = "";
              if (menuBtn) menuBtn.setAttribute("aria-expanded", "false");
            }
          }
        });
      })(allLangs[i]);
    }
  }

  /* ========== COOKIE CONSENT ========== */

  var cookiePrefs = {
    necessary: true,
    preferences: false,
    statistics: false,
    marketing: false,
  };

  function showCookieModal() {
    var backdrop = document.getElementById("cookie-backdrop");
    var modal = document.getElementById("cookie-modal");
    if (backdrop) backdrop.classList.remove("hidden");
    if (modal) modal.classList.remove("hidden");
  }

  function hideCookieModal() {
    var backdrop = document.getElementById("cookie-backdrop");
    var modal = document.getElementById("cookie-modal");
    if (backdrop) backdrop.classList.add("hidden");
    if (modal) modal.classList.add("hidden");
  }

  function saveCookieConsent(prefs) {
    try {
      localStorage.setItem(COOKIE_CONSENT_KEY, JSON.stringify(prefs));
    } catch (e) { /* private browsing */ }
    hideCookieModal();
  }

  /** Update toggle UI to reflect current cookiePrefs state */
  function updateToggleUI(toggleBtn) {
    var key = toggleBtn.getAttribute("data-cookie-toggle");
    var isOn = cookiePrefs[key];
    var track = toggleBtn.querySelector(".cookie-toggle-track");
    var thumb = toggleBtn.querySelector(".cookie-toggle-thumb");

    if (track) {
      track.style.backgroundColor = isOn ? "#02033b" : "";
      if (isOn) {
        track.classList.remove("bg-gray-300");
        track.classList.add("bg-[#02033b]");
      } else {
        track.classList.remove("bg-[#02033b]");
        track.classList.add("bg-gray-300");
      }
    }
    if (thumb) {
      if (isOn) {
        thumb.style.left = "23px";
      } else {
        thumb.style.left = "3px";
      }
    }
  }

  function initCookieConsent() {
    // Check if consent already given
    var consent = null;
    try {
      consent = localStorage.getItem(COOKIE_CONSENT_KEY);
    } catch (e) { /* private browsing */ }

    if (!consent) {
      showCookieModal();
    }

    // Tab switching
    var tabs = document.querySelectorAll("[data-cookie-tab]");
    for (var i = 0; i < tabs.length; i++) {
      (function (tab) {
        tab.addEventListener("click", function () {
          var target = tab.getAttribute("data-cookie-tab");

          // Update tab styles
          for (var j = 0; j < tabs.length; j++) {
            if (tabs[j].getAttribute("data-cookie-tab") === target) {
              tabs[j].classList.remove("border-transparent", "text-[#02033b]/50");
              tabs[j].classList.add("border-[#02033b]", "text-[#02033b]");
            } else {
              tabs[j].classList.remove("border-[#02033b]", "text-[#02033b]");
              tabs[j].classList.add("border-transparent", "text-[#02033b]/50");
            }
          }

          // Show/hide panels
          var panels = document.querySelectorAll(".cookie-panel");
          for (var k = 0; k < panels.length; k++) {
            panels[k].classList.add("hidden");
          }
          var activePanel = document.getElementById("cookie-panel-" + target);
          if (activePanel) activePanel.classList.remove("hidden");
        });
      })(tabs[i]);
    }

    // Toggle switches
    var toggles = document.querySelectorAll("[data-cookie-toggle]");
    for (var t = 0; t < toggles.length; t++) {
      (function (toggle) {
        toggle.addEventListener("click", function () {
          var key = toggle.getAttribute("data-cookie-toggle");
          cookiePrefs[key] = !cookiePrefs[key];
          updateToggleUI(toggle);
        });
      })(toggles[t]);
    }

    // Reject button
    var rejectBtn = document.getElementById("cookie-reject");
    if (rejectBtn) {
      rejectBtn.addEventListener("click", function () {
        saveCookieConsent({
          necessary: true,
          preferences: false,
          statistics: false,
          marketing: false,
        });
      });
    }

    // Accept Selected button
    var acceptSelectedBtn = document.getElementById("cookie-accept-selected");
    if (acceptSelectedBtn) {
      acceptSelectedBtn.addEventListener("click", function () {
        saveCookieConsent({
          necessary: true,
          preferences: cookiePrefs.preferences,
          statistics: cookiePrefs.statistics,
          marketing: cookiePrefs.marketing,
        });
      });
    }

    // Accept All button
    var acceptAllBtn = document.getElementById("cookie-accept-all");
    if (acceptAllBtn) {
      acceptAllBtn.addEventListener("click", function () {
        saveCookieConsent({
          necessary: true,
          preferences: true,
          statistics: true,
          marketing: true,
        });
      });
    }
  }

  /* ========== INIT ========== */

  initLocale();
  initLanguageSwitcher();
  initCookieConsent();

  // Expose setLocale globally for any page-specific needs
  window.gardablickI18n = {
    setLocale: setLocale,
    t: t,
    applyTranslations: applyTranslations,
  };
})();
