# mc1r-api-explorer
A Python script that queries bioinformatics databases using RESTful APIs. Exploring the gene responsible for red hair: MC1R.


## How-To-Run
*An active internet connection is required to connect the remote databases.*
1. Navigate to the directory containing mc1r_query.py

2. Run the following command:
**python3 mc1r_query.py**

## Included Files
* mc1r_query.py

## Output Files
* mc1r_sequence.fasta
* mc1r_homology_list.txt

## Reflection 

What you learned about working with RESTful APIs and biological web services that you did not know before this assignment.
> I had no idea that these systems even existed before this assignment. I'm blown away that they are free and easily accessible. I would have assumed information like this would be locked behind a massive pay wall, only allowing large corporations to access them. The API systems were surprisingly easy to search and filter results.

One part of the workflow that you found most challenging (for example, handling JSON responses, writing FASTA files, finding the longest ORF, using Biopython) and how you worked through that challenge.
> I thought connecting to the servers was the most difficult part. There is a very specific format that needs to be followed, and it is different depending on the RESTful API. It took a lot of trial and error to get the correct layout and specific wording needed for the filtering to work. I had to search for lots of examples and emulate the format I wanted.

How do you see this type of programmatic access to databases and sequence manipulation connecting to your own research interests or future work in bioinformatics.
> In the future, I see myself using these databases on a regular basis. I have an interest in microbiology and evolution, so using databases, I can see myself determining relation between species by their genes. Even if that isn’t the route I take in my career, simply pulling genomic information from a server directly into any script is going to be a regular occurrence.


## AI Use Disclosure

What AI tool did you use?
> Google Gemini

What did you use it for?
> It was helpful for finding information on Python commands, code structure, and debugging errors. I use it as a search assistant. After running into an issue that I can’t solve, I will often search Google for my problem. Usually, Gemini is first to pop up with helpful examples, sites, and forums that answer my exact question. 

How did you verify or edit its output?
> Most outputs are followed by websites that I can visit. They usually pertain to my question, or they are details on how to use the command in question. Here I can verify that the information it gives me is backed by credible sources.
