function solution(array, commands) {
  return commands.map((command) => {
    return array.slice(command[0] - 1, command[1]).sort((x, y) => x - y)[
      command[2] - 1
    ];
  });
}
