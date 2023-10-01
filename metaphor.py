
import os
import openai
from metaphor_python import Metaphor

# Initialize Metaphor API client with your API key
api_key = '35284399-1a30-4d82-9221-d8d5dfbff294'
metaphor = Metaphor(api_key)

# Define user question with a specific case
USER_QUESTION = "What are the recent court cases related to Case XYZ?"

# Define system message for generating search queries
SYSTEM_MESSAGE = "You are a helpful assistant that generates search queries based on user questions. Only generate one search query."

# Generate search query using OpenAI's GPT-3.5 Turbo
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": USER_QUESTION},
    ],
)

# Extract the generated search query
query = completion.choices[0].message.content

# Search for recent court cases using Metaphor API
search_response = metaphor.search(
    query, use_autoprompt=True, start_published_date="2023-01-01", end_published_date="2023-09-28"
)

# Print URLs of search results
print(f"URLs: {[result.url for result in search_response.results]}\n")

# Get contents for the first result
contents_result = search_response.get_contents()
first_result = contents_result.contents[0]

# Define system message for summarizing content
SYSTEM_MESSAGE = "You are a helpful assistant that summarizes the content of a webpage. Summarize the users input."

# Generate summary using OpenAI's GPT-3.5 Turbo
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": first_result.extract},
    ],
)

# Extract the generated summary
summary = completion.choices[0].message.content

# Print summary for the first result
print(f"Summary for {first_result.title}: {summary}")

