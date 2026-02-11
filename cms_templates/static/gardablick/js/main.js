/**
 * Gardablick — Main JavaScript
 * Page loader, header scroll behavior, mobile menu, hero search navigation
 */
(function () {
  "use strict";

  /* ========== PAGE TRANSITION LOADER ========== */
  var loader = document.getElementById("page-loader");

  function hideLoader() {
    if (!loader) return;
    loader.classList.add("fade-out");
    setTimeout(function () {
      loader.style.display = "none";
    }, 500);
  }

  function showLoader() {
    if (!loader) return;
    loader.classList.remove("fade-out");
    loader.style.display = "";
  }

  // Hide loader once the page is fully loaded
  window.addEventListener("load", function () {
    setTimeout(hideLoader, 600);
  });

  // Show loader when clicking internal links
  document.addEventListener("click", function (e) {
    var anchor = e.target.closest("a");
    if (!anchor) return;
    var href = anchor.getAttribute("href");
    if (
      !href ||
      href.charAt(0) === "#" ||
      href.indexOf("mailto:") === 0 ||
      href.indexOf("tel:") === 0 ||
      href.indexOf("http") === 0 ||
      anchor.getAttribute("target") === "_blank"
    ) return;
    // Internal navigation — show loader
    showLoader();
  }, true);

  /* ========== HEADER SCROLL BEHAVIOR ========== */
  var header = document.getElementById("gb-header");
  var logoWhite = document.getElementById("header-logo-white");
  var logoBlack = document.getElementById("header-logo-black");

  if (header) {
    var SCROLL_THRESHOLD = 50;

    function handleScroll() {
      var scrolled = window.scrollY > SCROLL_THRESHOLD;
      header.classList.toggle("scrolled", scrolled);

      if (logoWhite && logoBlack) {
        logoWhite.style.display = scrolled ? "none" : "";
        logoBlack.style.display = scrolled ? "" : "none";
      }
    }

    window.addEventListener("scroll", handleScroll, { passive: true });
    handleScroll();
  }

  /* ========== MOBILE MENU TOGGLE ========== */
  var menuBtn = document.getElementById("mobile-menu-btn");
  var mobileMenu = document.getElementById("mobile-menu");

  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener("click", function () {
      var isOpen = menuBtn.getAttribute("aria-expanded") === "true";
      menuBtn.setAttribute("aria-expanded", String(!isOpen));

      if (isOpen) {
        mobileMenu.classList.add("translate-x-full");
        mobileMenu.classList.remove("translate-x-0");
        document.body.style.overflow = "";
      } else {
        mobileMenu.classList.remove("translate-x-full");
        mobileMenu.classList.add("translate-x-0");
        document.body.style.overflow = "hidden";
      }
    });
  }

  /* ========== HERO SEARCH (Homepage) ========== */
  var heroSearchBtn = document.getElementById("hero-search-btn");

  if (heroSearchBtn) {
    heroSearchBtn.addEventListener("click", function () {
      var params = new URLSearchParams();

      var mun = document.querySelector('select[name="municipality"]');
      var price = document.querySelector('select[name="price_range"]');
      var type = document.querySelector('select[name="property_type"]');

      if (mun && mun.value && mun.value !== "all") {
        params.set("location", mun.value);
      }
      if (price && price.value && price.value !== "all") {
        if (price.value === "1000000+") {
          params.set("price_min", "1000000");
        } else {
          var parts = price.value.split("-");
          if (parts[0]) params.set("price_min", parts[0]);
          if (parts[1]) params.set("price_max", parts[1]);
        }
      }
      if (type && type.value && type.value !== "all") {
        params.set("property_type", type.value);
      }

      var listingsUrl = heroSearchBtn.getAttribute("data-listings-url") || "/immobili/";
      var query = params.toString();
      window.location.href = listingsUrl + (query ? "?" + query : "");
    });
  }
})();
