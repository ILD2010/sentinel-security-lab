const sidebar = document.getElementById("sidebar");
const toggle = document.getElementById("sidebar-toggle");

toggle.addEventListener("click", function () {

    sidebar.classList.toggle("collapsed");

    const isExpand = !sidebar.classList.contains("collapsed");

    toggle.setAttribute("aria-expanded", String(isExpanded))
})