// place files you want to import through the `$lib` alias in this folder.
export interface Question {
	id: number;
	Q: string;
	correct_option: string;
	options: {
		[key: string]: string;
	};
}
