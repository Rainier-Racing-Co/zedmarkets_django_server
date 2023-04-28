import requests

def horse_query(horse_id):
    
    base_url = "https://zed-ql.zed.run/graphql"

    query = """
    query($input: HorseInput) {
        horse(input: $input) {
            name
            nft_id
            img_url
            gen
            bloodline
            breed_type
            color
            inserted_at
            super_coat
            horse_type
            race_statistic {
                first_place_finishes
                second_place_finishes
                third_place_finishes
                number_of_races
                win_rate
                number_of_free_races
                number_of_paid_races
                free_win_rate
                paid_win_rate
                positions_per_distance {
                    distance
                    positions{
                        frequency
                        position
                    }
                }
            }
            parents{
                name
                nft_id
                horse_type
            }
            offsprings{
                name
                nft_id
                horse_type
            }
        }
    }
    """

    variables = {
        "input": {
            "horse_id": horse_id
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "query": query,
        "variables": variables
    }

    # Execute the POST query to GraphQL endpoint
    response = requests.post(base_url, json=payload, headers=headers)

    # Transform data into json format
    summary_horse_data = response.json()

    return summary_horse_data['data']['horse']

if __name__ == "__main__":
    horse = horse_query(8919)
    print(horse)
