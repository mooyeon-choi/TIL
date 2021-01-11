const api = () => {
  return fetch(
    `https://api.thecatapi.com/v1/images/search?limit=20`
  ).then((res) => res.json());
};
