// ==================
// Scroll top button - START
// ==================

const scrollToTopBtn = document.getElementById("scrollToTopBtn");
const rootElement = document.documentElement;

function scrollFunction() {
  if (document.body.scrollTop > 100 || rootElement.scrollTop > 100) {
    scrollToTopBtn.style.display = "block";
  } else {
    scrollToTopBtn.style.display = "none";
  }
}

// When the user scrolls down 100px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction()
};

// When the user clicks on the button, scroll to the top of the document
function scrollToTop() {
  // Scroll to top logic
  rootElement.scrollTo({
    top: 0,
    behavior: "smooth"
  })
}

scrollToTopBtn.addEventListener("click", scrollToTop)
// ...Scroll top button - END

// *******************************************************
// Walking snake behavior
const INITIAL_SNAKE_STATE = "walking-snake ld ld-breath";

const walkingSnake = document.querySelector("#walkingSnake");
const walkingContainer = document.querySelector("#walkingContainer");
const codeArea = document.querySelector('code.language-python');
const focusEvent = new Event('focus');
const blurEvent = new Event('blur');

// Select the node that will be observed for mutations
const fillableTooltip = document.querySelector('#tooltip');

// Options for the observer (which mutations to observe)
const config = {
  childList: true,
};

let walkingSnakeRect = {x: 0, y: 0};
let walkingContainerRect = {x: 0, y: 0};

let stepSize = 0;
let tooltipContent = {
  import: 'Try `import __hello__` in Python interpreter',
  from: 'from',
  as: 'as',
  def: 'ccc',
  datetime: '<a href="https://data.iana.org/time-zones/tz-link.html">tz-link</a>',
};

try {
  walkingSnake.style.left = "0px";
  walkingSnake.style.top = "0px";
  walkingSnake.className = INITIAL_SNAKE_STATE;
} catch (e) {
  // pass
}

const moveUp = () => {
  // Hide the tooltip
  walkingSnake.dispatchEvent(blurEvent);

  walkingSnakeRect = walkingSnake.getBoundingClientRect();
  walkingContainerRect = walkingContainer.getBoundingClientRect();

  if (walkingSnakeRect.y <= walkingContainerRect.y) {
    return;
  }

  walkingSnake.style.top = parseInt(walkingSnake.style.top) - stepSize + "px";
};

const moveDown = () => {
  // Hide the tooltip
  walkingSnake.dispatchEvent(blurEvent);

  walkingSnakeRect = walkingSnake.getBoundingClientRect();
  walkingContainerRect = walkingContainer.getBoundingClientRect();

  if (walkingSnakeRect.bottom + (walkingSnakeRect.height * 3) >= window.outerHeight) {
    return;
  }

  walkingSnake.style.top = parseInt(walkingSnake.style.top) + stepSize + "px";
};

const moveLeft = () => {
  // Hide the tooltip
  walkingSnake.dispatchEvent(blurEvent);

  walkingSnakeRect = walkingSnake.getBoundingClientRect();
  walkingContainerRect = walkingContainer.getBoundingClientRect();

  if (walkingSnakeRect.x <= walkingContainerRect.x + walkingSnakeRect.width) {
    return;
  }

  walkingSnake.style.left = parseInt(walkingSnake.style.left) - stepSize + "px";
};

const moveRight = () => {
  // Hide the tooltip
  walkingSnake.dispatchEvent(blurEvent);

  walkingSnakeRect = walkingSnake.getBoundingClientRect();
  walkingContainerRect = walkingContainer.getBoundingClientRect();

  if (walkingSnakeRect.x >= walkingContainerRect.right - (walkingSnakeRect.width * 2)) {
    return;
  }

  walkingSnake.style.left = parseInt(walkingSnake.style.left) + stepSize + "px";
};

const dispatchTooltipContent = () => {
  let selection = window.getSelection();
  let tooltipText = '';

  selection.modify('move', 'backward', 'word');
  selection.modify('extend', 'forward', 'word');

  tooltipText = tooltipContent[selection.toString()];

  if (tooltipText === undefined) {
    fillableTooltip.innerHTML = 'Look more ;))';
    return;
  }

  fillableTooltip.innerHTML = tooltipText;
};

document.body.onkeydown = (e) => {
  if (e.repeat) {
    stepSize++;
  } else {
    stepSize = 10;
  }

  switch (e.key) {
    case 'ArrowLeft':
    case 'A':
    case 'a':
      moveLeft();
      break;
    case 'ArrowUp':
    case 'W':
    case 'w':
      moveUp();
      break;
    case 'ArrowRight':
    case 'D':
    case 'd':
      moveRight();
      break;
    case 'ArrowDown':
    case 'S':
    case 's':
      moveDown();
      break;
  }
}

const spinSnake = () => {
  walkingSnake.className = "";
  walkingSnake.className = "walking-snake ld ld-spin-fast";

  setTimeout(function () {
    walkingSnake.className = INITIAL_SNAKE_STATE;
  }, 1000);
};

document.body.addEventListener('click', (e) => {
  if (walkingSnake.contains(e.target)) {
    spinSnake();
  } else if (codeArea.contains(e.target)) {
    dispatchTooltipContent();
  } else {
    // Hide the tooltip
    walkingSnake.dispatchEvent(blurEvent);
  }
});

// Callback function to execute when mutations are observed
const callback = function (mutationsList) {

  // Use traditional 'for loops' for IE 11
  for (const mutation of mutationsList) {
    if (mutation.type === 'childList') {
      // Make the tooltip visible
      walkingSnake.dispatchEvent(focusEvent);
    }
  }
};

// Create an observer instance linked to the callback function
const observer = new MutationObserver(callback);


try {
  // Start observing the target node for configured mutations
  observer.observe(fillableTooltip, config);
} catch (e) {
  // pass
}

