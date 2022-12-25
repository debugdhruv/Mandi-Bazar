function changeCss() {
    var headerElement = document.getElementById("header");
    var logo = document.getElementById("navlogo");
    var link1 = document.getElementById("navlink1");
    var link2 = document.getElementById("navlink2");
    var link3 = document.getElementById("navlink3");
    var link4 = document.getElementById("navlink4");
    var link5 = document.getElementById("navlink5");

    console.log(this.scrollY);
    var pos = this.scrollY;
    if (pos == 0) {
        // headerElement.style.backgroundColor = "transparent";
        headerElement.setAttribute("style", "box-shadow: 0px 0px 0px 0px #111; background-color:blue;")
        logo.setAttribute("src", "/static/Images/logo.png");
        link1.style.color = "white";
        link2.style.color = "white";
        link3.style.color = "white";
        link4.style.color = "white";
        link5.style.color = "white";

    }
    else {
        // headerElement.style.backgroundColor = "white";
        headerElement.setAttribute("style", "box-shadow: 0px 15px 10px -15px #111; background-color:white;");
        logo.setAttribute("src", "/static/Images/colored-logo.png");
        link1.style.color = "black";
        link2.style.color = "black";
        link3.style.color = "black";
        link4.style.color = "black";
        link5.style.color = "black";
    }
}


window.addEventListener("scroll", changeCss, false);