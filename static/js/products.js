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
  
  setInterval(() => {
    carousel.innerHTML = ""
    const container = document.createElement("span")
    const random = Math.floor(Math.random() * lists.length)
    container.textContent = lists[random]
    carousel.appendChild(container)
  }, 2500)

}

window.onload = () => {
  functionCarousel()
}
