#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
	return len(string) % 2 == 0


def get_num_char(string, char):
	result = 0
	for i in range(len(string)):
		if string[i] == char:
			result += 1
	return result


def get_first_part_of_name(name):
	first_Part = name.split("-")[0]
	capitalized = first_Part[0].upper() + first_Part[1:]
	return "Bonjour, " + capitalized


def get_random_sentence(animals, adjectives, fruits):
	basicSentence ="Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s."

	animal = animals[random.randrange(0, len(animals))]
	adjective = adjectives[random.randrange(0, len(adjectives))]
	fruit = fruits[random.randrange(0, len(fruits))]
	return basicSentence % (animal, adjective, fruit)


if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
