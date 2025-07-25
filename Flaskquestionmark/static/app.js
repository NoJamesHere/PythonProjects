function showInput() {
  const input = document.getElementById('userInput').value;
  fetch('/api/echo', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ msg: input })
  })
    .then(res => res.json())
    .then(() => {
      // After echo, fetch the encrypted version
      return fetch('/api/greet');
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById('test').textContent = data.message;
      console.log('Encrypted:', data.message);
    })
    .catch(err => console.error('Error:', err));
}
// GET from /api/greet

fetch('/api/greet')
  .then(res => res.json())
  .then(data => {
    document.getElementById('test').textContent = data.message;
    console.log('Greet:', data.message);
  })
  .catch(err => console.error('Fetch error:', err));

