document.addEventListener("DOMContentLoaded", function () {
  let currentLocation = new URL(window.location).pathname;

  // endpoints and id of element which will be set active
  let endpoints = new Map([
    ["/", "home"],
    ["/projekty", "projects"],
    ["/fotky", "media"],
    ["/videa", "media"],
    ["/koncerty", "concerts"],
    ["/kontakt", "contact"],
    ["/o_me", "about_me"]
  ])

  // adding css class to element
  for (const [key, value] of endpoints.entries()){
    if (currentLocation === key){
      let element = this.getElementById(value)
      element.classList.add("active-nav")
    }
  }


  
});
