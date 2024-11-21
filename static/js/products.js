"use strict";

const functionCarousel = () => {
  const carousel = document.getElementById("carousel");
  let random = 0;
  const img = document.createElement("img");
  // const random = Math.floor(Math.random() * imgs.length);
  // carousel.style.backgroundImage = `url('${imgs[random]}')`;
  img.src = imgs[random % imgs.length];
  carousel.appendChild(img);
  setInterval(() => {
    carousel.innerHTML = "";
    random++;
    const img = document.createElement("img");
    // const random = Math.floor(Math.random() * imgs.length);
    // carousel.style.backgroundImage = `url('${imgs[random]}')`;
    img.src = imgs[random % imgs.length];

    carousel.appendChild(img);
  }, 2500);
};

window.onload = () => {
  functionCarousel();
};
