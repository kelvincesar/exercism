type WordsInput = {
  [key: string]: string[]
};

type WordsOutput = {
  [key: string]: number
};


export function transform(input: WordsInput): WordsOutput {
  const result: WordsOutput = {};

  for (const [score, letters] of Object.entries(input)) {
    for (const letter of letters) {
      result[letter.toLowerCase()] = Number(score)
    }
  }

  return result;
}
