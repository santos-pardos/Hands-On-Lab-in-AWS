## Steps

https://alvintoh.gitbook.io/apache-2-0-spark-with-scala/section-5-running-spark-on-a-cluster/35.-creating-similar-movies-from-one-million-ratings-on-emr

https://grouplens.org/datasets/movielens/

Create Cluster:  Spark Spark 1.6.2 Hadoop 2.7.2 YARN with Ganglia 3.7.2.  Switch on logs options in the cluster.


Connect EC2 

    ls
 
    pwd

    aws s3 cp s3://sundog-spark/MovieSimilarities1M.jar ./

    

    ls

    aws s3 cp s3://sundog-spark/ml-1m/movies.dat ./

    ls

    

    spark-submit MovieSimilarities1M.jar 260
