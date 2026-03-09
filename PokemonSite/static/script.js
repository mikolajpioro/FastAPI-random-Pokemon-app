async function getRandomPokemon() {
    // Pick a random ID between 1 and 1025
    const randomId = Math.floor(Math.random() * 1025) + 1;
    
    try {
        // Fetch data from PokeAPI
        const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${randomId}`);
        const data = await response.json();
        
        // Update the HTML elements
        document.getElementById('pokemon_name').innerText = data.name;
        document.getElementById('pokemon_id').innerText = `#${data.id}`;
    
        // Update the sprite
        const spriteUrl = data.sprites.other['official-artwork'].front_default;
        document.getElementById('pokemon_sprite').src = spriteUrl;
        
    } catch (error) {
        console.error("Error fetching Pokémon:", error);
    }
}