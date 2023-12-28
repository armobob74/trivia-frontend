import { localStorageStore } from '@skeletonlabs/skeleton';
import type { Writable } from 'svelte/store';

export const playersStore: Writable<any> = localStorageStore('players', []);
