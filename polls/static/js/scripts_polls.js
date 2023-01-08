


function closeNav() {
  document.getElementById("mySidenav").style.display = "none";
  document.getElementById("pembatas").style.marginLeft = "0px";
  document.getElementById("content_polls").style.marginLeft="5px";
  document.getElementById("content_polls").style.paddingLeft="100px";
  document.getElementById("fotterest").style.marginLeft="0px";

}


document.getElementsByClassName('pembatas')[0]
        .addEventListener('click', function (event) {
            document.getElementById("mySidenav").style.display = "block";
            document.getElementById("pembatas").style.marginLeft = "200px";
            document.getElementById("content_polls").style.marginLeft="205px";
            document.getElementById("content_polls").style.paddingLeft="40px";
            document.getElementById("fotterest").style.marginLeft="200px";
});

