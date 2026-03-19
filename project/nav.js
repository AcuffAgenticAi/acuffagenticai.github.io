/**
 * nav.js — Acuff Agentic AI · Control Tower
 * Injects the shared header/nav and footer into every page.
 * Active link is auto-detected from the current filename.
 */

(function () {
  const links = [
    { href: 'index.html',        label: 'Home' },
    { href: 'product.html',      label: 'Product' },
    { href: 'category.html',     label: 'Category' },
    { href: 'architecture.html', label: 'Architecture' },
    { href: 'vision.html',       label: 'Vision' },
    { href: 'founder.html',      label: 'Founder' },
    { href: 'investors.html',    label: 'Investors' },
    { href: 'displays.html',     label: 'Displays' },
    { href: 'press.html',        label: 'Press' },
    { href: 'contact.html',      label: 'Contact' },
  ];

  const current = window.location.pathname.split('/').pop() || 'index.html';

  const navHTML = links
    .map(l => `<a href="${l.href}"${current === l.href ? ' class="active"' : ''}>${l.label}</a>`)
    .join('');

  const headerHTML = `
<header>
  <a href="index.html" class="logo">
    Acuff Agentic AI
    <span>Control Tower</span>
  </a>
  <nav>${navHTML}</nav>
</header>`;

  const footerHTML = `
<footer>
  <div class="footer-logo">Acuff Agentic AI</div>
  <div class="footer-links">
    <a href="product.html">Product</a>
    <a href="architecture.html">Architecture</a>
    <a href="displays.html">Displays</a>
    <a href="contact.html">Contact</a>
  </div>
  <div>© 2025 Acuff Agentic AI · Oversight for the age of autonomous systems</div>
</footer>`;

  // Inject header before body content
  const navEl = document.querySelector('nav');
  if (navEl && navEl.parentElement === document.body) {
    // bare <nav></nav> placeholder — replace with full header
    navEl.outerHTML = headerHTML;
  } else if (!document.querySelector('header')) {
    document.body.insertAdjacentHTML('afterbegin', headerHTML);
  }

  // Inject footer
  if (!document.querySelector('footer')) {
    document.body.insertAdjacentHTML('beforeend', footerHTML);
  }
})();
