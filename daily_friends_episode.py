from random import randint

number_of_episodes = [24,24,25,24,24,25,24,24,24,17]

def get_random_episode():
	season = randint(1,10)
	episode = randint(1,number_of_episodes[season-1])
	print 'Today\'s episode is Season {0} Episode {1}'.format(season, episode)

if __name__ == "__main__":
	get_random_episode()