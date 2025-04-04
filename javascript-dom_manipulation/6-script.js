
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
 
    return response.json();
  })
  .then(data => {
    
    const characterName = data.name;

    
    const characterElement = document.querySelector('#character');
    characterElement.textContent = characterName;
  })
  .catch(error => {
    
    console.error('There was a problem with the fetch operation:', error);
  });