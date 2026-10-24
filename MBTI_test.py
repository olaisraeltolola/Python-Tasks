def take_test():
	name = input("What is your name\n")
	
	repeat = True


	question_options = [
				[("A. Interact with many, including strangers"), ("B. Interact with a few, known to you")], 
				[("A. Realistic than speculative"), ("B. Speculative than realistic")], 
				[("A. Have your “head in the clouds”"), ("B. Be “in a rut”")], 
				[("A. Principles"), ("B. Emotions")], 
				[("A. Convincing"), ("B. Touching")], 
				[("A. To deadlines"), ("B. Just “whenever”")], 
				[("A. Rather carefully"), ("B. Somewhat impulsively")], 
				[("A. Stay late, with increasing energy"), ("B. Leave early with decreased energy")], 
				[("A. Sensible people"), ("B. Imaginative people")], 
				[("A. What is actual"), ("B. What is possible ")], 
				[("A. Laws than circumstances"), ("B. Circumstances than laws")], 
				[("A. Objective"), ("B. Personal")], 
				[("A. Punctual"), ("B. Leisurely")], 
				[("A. Incomplete"), ("B. Completed")], 
				[("A. Keep abreast of other’s happenings"), ("B. Get behind on the news")], 
				[("A. Do it the usual way"), ("B. Do it your own way")], 
				[("A. “Say what they mean and mean what they say”"), ("B. Express things more by use of analogy")], 
				[("A. Consistency of thought"), ("B. Harmonious human relationships")], 
				[("A. Logical judgments"), ("B. Value judgments")], 
				[("A. Settled and decided"), ("B. Unsettled and undecided")]
	]



	questions = [
			("1. At a party do you:"), 
			("2. Are you more:"), 
			("3. Is it worse to:"), 
			("4. Are you more impressed by:"), 
			("5. Are more drawn toward the:"), 
			("6. Do you prefer to work:"), 
			("7. Do you tend to choose:"), 
			("8. At parties do you:"), 
			("9. Are you more attracted to:"), 
			("10. Are you more attracted to:"), 
			("11. In judging others are you more swayed by:"), 
			("12. In approaching others is your inclination to be somewhat:"), 
			("13. Are you more:"), ("14. Does it bother you more having things:"), 
			("15. In your social groups do you:"), 
			("16. In doing ordinary things are you more likely to:"), 
			("17. Writers should:"), 
			("18. Which appeals to you more:"), 
			("19. Which appeals to you more:"), 
			("20. Do you want things:")
	]



	first_segment_print_out = ""
	second_segment_print_out = ""
	third_segment_print_out = ""
	fourth_segment_print_out = ""

	index = 0
	question_choice = ""
	count_a_for_first_segment = 0
	count_b_for_first_segment = 0
	count_a_for_second_segment = 0
	count_b_for_second_segment = 0
	count_a_for_third_segment = 0
	count_b_for_third_segment = 0
	count_a_for_fourth_segment = 0
	count_b_for_fourth_segment = 0


	for question in questions:

		print(question)

		for second_index in range(len(question_options[0])):
			print(f"{question_options[index][second_index]}")

		question_choice = input().lower()
			
		print()

		
		while is_input_valid(question_choice) == False:
			print("Expected an A or B, please try again")

			print(question)

			for second_index in range(len(question_options[0])):
				print(f"{question_options[index][second_index]}")

			question_choice = input().lower()
			
			print()


		if (index + 1) == 1 or (index + 1) == 5 or (index + 1) == 9 or (index + 1) == 13 or (index + 1) == 17:
			if question_choice == "a":
				first_segment_print_out += question_options[index][0] + "\n"
				count_a_for_first_segment += 1
			elif question_choice == "b":
				first_segment_print_out += question_options[index][1] + "\n"
				count_b_for_first_segment += 1


		elif (index + 1) == 2 or (index + 1) == 6 or (index + 1) == 10 or (index + 1) == 14 or (index + 1) == 18:
			if question_choice == "a":
				second_segment_print_out += question_options[index][0] + "\n"
				count_a_for_second_segment += 1
			elif question_choice == "b":
				second_segment_print_out += question_options[index][1] + "\n"
				count_b_for_second_segment += 1


		if (index + 1) == 3 or (index + 1) == 7 or (index + 1) == 11 or (index + 1) == 15 or (index + 1) == 19:
			if question_choice == "a":
				third_segment_print_out += question_options[index][0] + "\n"
				count_a_for_third_segment += 1
			elif question_choice == "b":
				third_segment_print_out += question_options[index][1] + "\n"
				count_b_for_third_segment += 1


		if (index + 1) == 4 or (index + 1) == 8 or (index + 1) == 12 or (index + 1) == 16 or (index + 1) == 20:
			if question_choice == "a":
				fourth_segment_print_out += question_options[index][0] + "\n"
				count_a_for_fourth_segment += 1
			elif question_choice == "b":
				fourth_segment_print_out += question_options[index][1] + "\n"
				count_b_for_fourth_segment += 1


		index += 1


	result = ""
	if count_a_for_first_segment > count_b_for_first_segment:
		result += "E"
	else: result += "I"


	if count_a_for_second_segment > count_b_for_second_segment:
		result += "S"
	else: result += "N"


	if count_a_for_third_segment > count_b_for_third_segment:
		result += "T"
	else: result += "F"


	if count_a_for_fourth_segment > count_b_for_fourth_segment:
		result += "J"
	else: result += "P"

	print (result)

	print()
	print(f"Hello {name}, you selected\n")
	print(f"{first_segment_print_out}Number of A selected: {count_a_for_first_segment}\nNumber of B selected: {count_b_for_first_segment}")
	print()
	print()

	print(f"{second_segment_print_out}Number of A selected: {count_a_for_second_segment}\nNumber of B selected: {count_b_for_second_segment}")
	print()
	print()

	print(f"{third_segment_print_out}Number of A selected: {count_a_for_third_segment}\nNumber of B selected: {count_b_for_third_segment}")
	print()
	print()

	print(f"{fourth_segment_print_out}Number of A selected: {count_a_for_fourth_segment}\nNumber of B selected: {count_b_for_fourth_segment}")
	print()



	if result == "INTJ":
		print(print_personality_INTJ(result))

	elif result == "INTP":
		print(print_personality_INTP(result))

	elif result == "ENTJ":
		print(print_personality_ENTJ(result))

	elif result == "ENTP":
		print(print_personality_ENTP(result))

	elif result == "INFJ":
		print(print_personality_INFJ(result))

	elif result == "INFP":
		print(print_personality_INFP(result))

	elif result == "ENFJ":
		print(print_personality_ENFJ(result))

	elif result == "ENFP":
		print(print_personality_ENFP(result))

	elif result == "ISTJ":
		print(print_personality_ISTJ(result))

	elif result == "ISFJ":
		print(print_personality_ISFJ(result))

	elif result == "ESTJ":
		print(print_personality_ESTJ(result))

	elif result == "ESFJ":
		print(print_personality_ESFJ(result))

	elif result == "ISTP":
		print(print_personality_ISTP(result))

	elif result == "ISFP":
		print(print_personality_ISFP(result))

	elif result == "ESTP":
		print(print_personality_ESTP(result))

	elif result == "ESFP":
		print(print_personality_ESFP(result))



def is_length_of_input_valid(letter):
	return len(letter) == 1

def is_input_A_or_B(letter):
	return letter == "a" or letter == "b"

def is_input_valid(letter):
	return is_length_of_input_valid(letter) and is_input_A_or_B(letter)


def print_personality_INTJ(personality):
	inference = '''

INTJ — The Architect
Introverted · Intuitive · Thinking · Judging
Meaning: Independent, strategic and future-oriented.

Inference: An INTJ may prefer to understand the big picture, develop a plan and work toward long-term goals. They often like competence, independence and efficiency.

Strengths: Strategic thinking, determination, problem-solving, independence.

Possible challenges: May appear distant, overly critical or too focused on perfection.

'''

	return inference

def print_personality_INTP(personality):
	inference = """

INTP — The Logician
Introverted · Intuitive · Thinking · Prospecting
Meaning: Curious, theoretical and analytical.

Inference: An INTP may enjoy understanding how things work, questioning assumptions and exploring complex ideas. They may value intellectual freedom.

Strengths: Creativity, logical reasoning, curiosity, originality.

Possible challenges: May overthink, procrastinate or struggle to finish projects.

"""

	return inference


def print_personality_ENTJ(personality):
	inference = """

ENTJ — The Commander
Extraverted · Intuitive · Thinking · Judging
Meaning: Decisive, ambitious and organized.

Inference: An ENTJ may naturally take initiative, coordinate people and seek efficient ways to achieve goals. They may enjoy leadership and solving large-scale problems.

Strengths: Leadership, planning, confidence, execution.

Possible challenges: May become impatient, domineering or dismissive of emotions.

"""

	return inference


def print_personality_ENTP(personality):
	inference = """

ENTP — The Debater
Extraverted · Intuitive · Thinking · Prospecting
Meaning: Inventive, curious and argumentative in the intellectual sense.

Inference: An ENTP may enjoy debating ideas, exploring alternatives and challenging conventional thinking. They may be energized by novelty.

Strengths: Adaptability, innovation, quick thinking, persuasion.

Possible challenges: May lose interest quickly, argue excessively or neglect routine responsibilities.


"""

	return inference


def print_personality_INFJ(personality):
	inference = """

INFJ — The Advocate
Introverted · Intuitive · Feeling · Judging
Meaning: Insightful, idealistic and purpose-driven.

Inference: An INFJ may look for deeper meanings in experiences, care about people's development and prefer relationships with depth.

Strengths: Empathy, insight, thoughtfulness, commitment.

Possible challenges: May overanalyze relationships, set unrealistic expectations or neglect personal needs.

"""

	return inference

def print_personality_INFP(personality):
	inference = """

INFP — The Mediator
Introverted · Intuitive · Feeling · Prospecting
Meaning: Imaginative, compassionate and values-driven.

Inference: An INFP may want their choices to align with their personal beliefs and may be drawn to creativity, self-expression and meaningful causes.

Strengths: Empathy, imagination, authenticity, idealism.

Possible challenges: May avoid conflict, take criticism personally or struggle to turn dreams into practical plans.

"""

	return inference


def print_personality_ENFJ(personality):
	inference = """

ENFJ — The Protagonist
Extraverted · Intuitive · Feeling · Judging
Meaning: Encouraging, people-oriented and inspiring.

Inference: An ENFJ may enjoy helping others develop, organizing group efforts and creating a sense of belonging.

Strengths: Communication, empathy, leadership, encouragement.

Possible challenges: May seek approval, overcommit or feel responsible for everyone's happiness.

"""

	return inference

def print_personality_ENFP(personality):
	inference = """

ENFP — The Campaigner
Extraverted · Intuitive · Feeling · Prospecting
Meaning: Enthusiastic, imaginative and expressive.

Inference: An ENFP may enjoy connecting with people, discovering opportunities and pursuing ideas that excite them. They may be motivated by freedom and purpose.

Strengths: Enthusiasm, creativity, warmth, adaptability.

Possible challenges: May become distracted, overcommit or struggle with consistency.

"""

	return inference


def print_personality_ISTJ(personality):
	inference = """

ISTJ — The Logistician
Introverted · Observant · Thinking · Judging
Meaning: Dependable, thorough and methodical.

Inference: An ISTJ may prefer clear expectations, evidence, established procedures and completing responsibilities carefully.

Strengths: Reliability, discipline, attention to detail, honesty.

Possible challenges: May resist change, be inflexible or focus too heavily on rules.

"""
	return inference


def print_personality_ISFJ(personality):
	inference = """

ISFJ — The Defender
Introverted · Observant · Feeling · Judging
Meaning: Caring, attentive and supportive.

Inference: An ISFJ may show love through practical help, remember personal details and value harmony and dependable relationships.

Strengths: Loyalty, patience, kindness, responsibility.

Possible challenges: May struggle to say no, suppress their needs or worry excessively about disappointing others.

"""

	return inference


def print_personality_ESTJ(personality):
	inference = """

ESTJ — The Executive
Extraverted · Observant · Thinking · Judging
Meaning: Practical, direct and organized.

Inference: An ESTJ may enjoy coordinating tasks, establishing order and ensuring that commitments are fulfilled.

Strengths: Organization, decisiveness, accountability, efficiency.

Possible challenges: May become controlling, impatient with ambiguity or too rigid about procedures.

"""

	return inference


def print_personality_ESFJ(personality):
	inference = """

ESFJ — The Consul
Extraverted · Observant · Feeling · Judging
Meaning: Sociable, considerate and community-minded.

Inference: An ESFJ may value cooperation, traditions and making others feel included. They may pay close attention to social expectations.

Strengths: Friendliness, helpfulness, cooperation, practical care.

Possible challenges: May worry about social judgment, seek reassurance or find disagreement uncomfortable.

"""

	return inference


def print_personality_ISTP(personality):
	inference = """

ISTP — The Virtuoso
Introverted · Observant · Thinking · Prospecting
Meaning: Resourceful, independent and hands-on.

Inference: An ISTP may prefer learning by doing, investigating how systems operate and solving practical problems independently.

Strengths: Troubleshooting, composure, adaptability, technical skills.

Possible challenges: May seem emotionally reserved, take unnecessary risks or become bored with long-term routines.

"""

	return inference


def print_personality_ISFP(personality):
	inference = """

ISFP — The Adventurer
Introverted · Observant · Feeling · Prospecting
Meaning: Artistic, gentle and individualistic.

Inference: An ISFP may value personal freedom, aesthetics and living according to their own values. They may express themselves more through actions or creativity than words.

Strengths: Sensitivity, creativity, kindness, flexibility.

Possible challenges: May avoid difficult conversations, struggle with planning or dislike restrictive environments.

"""

	return inference


def print_personality_ISFP(personality):
	inference = """

ISFP — The Adventurer
Introverted · Observant · Feeling · Prospecting
Meaning: Artistic, gentle and individualistic.

Inference: An ISFP may value personal freedom, aesthetics and living according to their own values. They may express themselves more through actions or creativity than words.

Strengths: Sensitivity, creativity, kindness, flexibility.

Possible challenges: May avoid difficult conversations, struggle with planning or dislike restrictive environments.

"""

	return inference


def print_personality_ESTP(personality):
	inference = """

ESTP — The Entrepreneur
Extraverted · Observant · Thinking · Prospecting
Meaning: Energetic, action-oriented and adaptable.

Inference: An ESTP may respond quickly to changing situations, enjoy exciting experiences and prefer practical solutions over extended theorizing.

Strengths: Confidence, negotiation, observation, resourcefulness.

Possible challenges: May act impulsively, underestimate risks or become impatient with lengthy planning.

"""

	return inference


def print_personality_ESFP(personality):
	inference = """

ESFP — The Entertainer
Extraverted · Observant · Feeling · Prospecting
Meaning: Expressive, enthusiastic and sociable.

Inference: An ESFP may enjoy shared experiences, bringing energy to a group and responding to what's happening in the present.

Strengths: Warmth, spontaneity, enthusiasm, social awareness.

Possible challenges: May seek immediate gratification, avoid unpleasant tasks or find long-term structure restrictive.

"""

	return inference


take_test()