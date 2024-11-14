"use strict"

const functionCarousel = () => {
  const carousel = document.getElementById("carousel")
  const lists = [
    "Cute pics mo",
    "Cute pics ko",
    "Long Short Message",
    "NGL na walang laman",
    "Spambot sa messenger",
    "Meta AI na binebe time",
    "AI na pagod"
  ]
  
  const container = document.createElement("span")
  
  setInterval(() => {
    const random = Math.floor(Math.random() * lists.length)
    container.textContent = lists[random]
  }, 2500)
  carousel.appendChild(container)
}

window.onload = () => {
  functionCarousel()
}
