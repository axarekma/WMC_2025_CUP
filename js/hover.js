document.addEventListener("DOMContentLoaded", function () {
  const scoreElements = document.querySelectorAll(
    ".score-hover[data-hover-image]"
  );

  const hoverImg = document.createElement("img");
  hoverImg.className = "hover-image";
  document.body.appendChild(hoverImg);

  scoreElements.forEach((element) => {
    const hoverImageUrl = element.getAttribute("data-hover-image");

    element.addEventListener("mouseenter", () => {
      hoverImg.src = hoverImageUrl;
      hoverImg.style.opacity = "0.95";
    });

    element.addEventListener("mousemove", (e) => {
      const offsetX = -150;
      const offsetY = 20;
      const padding = 20;

      const imageWidth = hoverImg.offsetWidth;
      const imageHeight = hoverImg.offsetHeight;

      let proposedLeft = e.clientX + offsetX;
      if (proposedLeft + imageWidth + padding > window.innerWidth) {
        proposedLeft = window.innerWidth - imageWidth - padding;
      }
      if (proposedLeft < padding) {
        proposedLeft = padding;
      }

      let proposedTop = e.clientY + offsetY;
      if (proposedTop + imageHeight + padding > window.innerHeight) {
        proposedTop = window.innerHeight - imageHeight - padding;
      }
      if (proposedTop < padding) {
        proposedTop = padding;
      }

      hoverImg.style.left = proposedLeft + "px";
      hoverImg.style.top = proposedTop + "px";
    });

    element.addEventListener("mouseleave", () => {
      hoverImg.style.opacity = "0";
    });
  });
});
