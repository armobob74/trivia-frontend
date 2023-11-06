// place files you want to import through the `$lib` alias in this folder.
export interface Question {
	[key: string]: string | number;
	text: string;
	A: string;
	B: string;
	C: string;
	D: string;
	correct: string;
	difficulty: number;
}

export let BACKEND_URL: string = 'http://localhost:5000';
