axios.get("https://jsonplaceholder.typicode.com/posts/1").then((response) => {
  console.log(response);
  document.write(`
        <h1>${response.data.id} : ${response.data.title}</h1>
        <p>${response.data.body}</p>
        `);
  return response.data;
});
console.log("bye");
