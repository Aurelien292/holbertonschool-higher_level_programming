fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    
    return response.json();
  })
  .then(data => {
    
    const helloElement = document.querySelector('#hello');
    
    
    helloElement.textContent = data.hello;
  })
  .catch(error => {
    
    console.error('There was a problem with the fetch operation:', error);
  });
