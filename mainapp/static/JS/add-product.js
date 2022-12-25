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
      headerElement.setAttribute("style", "box-shadow: 0px 0px 0px 0px #111; background-color:transparent;")
      logo.setAttribute("src", '/static/Images/logo.png');
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



var loadFile1 = function(event) {
	var image = document.getElementById('output1');
	image.src = URL.createObjectURL(event.target.files[0]);
};


var loadFile2 = function(event) {
	var image = document.getElementById('output2');
	image.src = URL.createObjectURL(event.target.files[0]);
};


var loadFile3 = function(event) {
	var image = document.getElementById('output3');
	image.src = "/static/Images/add-product/uploaded.png";
};


// document.getElementById("product-name").addEventListener("change", subtype);

// function subtype(){
//   var product = document.getElementById("product-name").value;
//   let products = [];
//   const element = document.getElementById("subtype");

//   if (product.toLowerCase()=="soyabean"){
//     products = ["2050 soyabean","93-05 soyabean", "95-60 soyabean","335 soyabean","80-21 soyabean"]
//   }
//   else if (product.toLowerCase()=="wheat"){
//     products = ["Logan Cross","VL-832","VL-804", "HS-365","HS-240","HD2687","WH-147","WH-542","PBW-343","WH-896(d)","PDW-233(d)","UP-2338"]
//   }
//   else if (product.toLowerCase()=="wheat"){
//     products = ["Logan Cross","VL-832","VL-804", "HS-365","HS-240","HD2687","WH-147","WH-542","PBW-343","WH-896(d)","PDW-233(d)","UP-2338"]
//   }

  
//       products.forEach(data => {
//       const para = document.createElement("option");
//       const node = document.createTextNode(data);
//       para.appendChild(node);
//       element.appendChild(para);
//       para.setAttribute('class', 'menu-item');
//     });

  
// }