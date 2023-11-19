// Side naviagation bar animations
var sidenavIsOpen = false;

function toggleNav() {
  var marginLeft;

  if (sidenavIsOpen) {
    marginLeft = "0px";
    sidenavIsOpen = false;
  }
  else {
    marginLeft = "200px";
    sidenavIsOpen = true;
  }

  document.getElementById("sidenav").style.width = marginLeft;
  document.getElementById("core").style.marginLeft = marginLeft;
}
