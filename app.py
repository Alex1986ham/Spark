import findspark
import pyspark
sc = pyspark.SparkContext(appName="maps_and_lazy_evaluation_example")

log_of_songs = [
        "Despacito",
        "Nice for what",
        "No tears left to cry",
        "Despacito",
        "Havana",
        "In my feelings",
        "Nice for what",
        "despacito",
        "All the stars"
]

# parallelize the log_of_songs to use with Spark
distributed_song_log = sc.parallelize(log_of_songs)



def convert_song_to_lowercase(song):
    return song.lower()

convert_song_to_lowercase("Havana")

# apply the map step on each song
distributed_song_log.map(convert_song_to_lowercase)

distributed_song_log.map(convert_song_to_lowercase).collect()

distributed_song_log.collect()

distributed_song_log.map(lambda song: song.lower()).collect()

distributed_song_log.map(lambda x: x.lower()).collect()
