
//for the last nav that was not showing when opening
const element = document.getElementById("scroll-to-view");
var myCollapsible = document.getElementById('navbarCollapseBottom')

myCollapsible.addEventListener('shown.bs.collapse', function () {
element.scrollIntoView();})



