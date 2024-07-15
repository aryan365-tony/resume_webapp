const wipeLayer = document.querySelector('.wipe-layer');

// set transform origin values based on current webpage
let originX, originY;
switch (window.location.pathname) {
  case '/':
    originX = '58%';
    originY = '51.5%';
    break;
  case '/edu-page':
    originX = '94%';
    originY = '51.5%';
    break;
  case '/por-page':
    originX = '83%';
    originY = '51.5%';
    break;
  case '/result-page':
    originX = '90%';
    originY = '51.5%';
    break;
  case '/projects-page':
    originX = '68%';
    originY = '51.5%';
    break;
  case '/work-page':
    originX = '62%';
    originY = '51.5%';
    break;
  case '/skills-page':
    originX = '74%';
    originY = '51.5%';
    break;

  case '/download-page':
    originX = '98%';
    originY = '51.5%';
    break;
  default:
    originX = '0%';
    originY = '0%';
}

wipeLayer.style.transformOrigin = `${originX} ${originY}`;

window.addEventListener('load', function() {
  setTimeout(function() {
    document.querySelector('.wipe-layer').classList.add('wipe-in');
    document.querySelector('.page-content').classList.add('visible');
  }, 0); // no delay, but you can add a delay if you want
});
