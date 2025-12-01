document.addEventListener('readystatechange', (event) => {
  if (event.target.readyState === 'complete') {
    console.log('Ready state complete - the page is ready');
    initApp();
  }
});

const initApp = () => {
    const view = document.querySelector('#view2');
    const div = view.querySelector('div');
    const h2 = div.querySelector('h2');


    const doSomething = () => {
    alert('Doing something');
    };


  view.addEventListener('click', (e) => {
  view.style.backgroundColor = 'purple';
}, true); // useCapture = true

// Stop bubbling at the DIV level
div.addEventListener('click', (e) => {
  e.stopPropagation(); // Event won't reach VIEW
  div.style.backgroundColor = 'blue';
}, false);

h2.addEventListener('click', (e) => {
  e.target.textContent = 'Clicked';
}, true);





};



