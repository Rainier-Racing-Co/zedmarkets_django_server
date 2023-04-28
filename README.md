# Horse Racing Stats API

This is an API that provides statistics for [ZED Run](https://zed.run) horses. The API retrieves data from the ZED Run GraphQL API and stores it in a local database using SQLite.

## Getting Started

To run the project locally, you will need to have Python 3 and Django installed on your machine. You can then follow these steps:

* Clone the repository: `git clone https://github.com/hfoley2013/zedmarkets_django_server.git`
* Navigate to the project directory: cd horse-racing-stats-api
* Install the dependencies: `pip install -r requirements.txt`
* Create a local database: `python manage.py migrate`
* Run the development server: `python manage.py runserver`

You should now be able to access the API at `http://localhost:8000/`.

## API Endpoints

The API provides the following endpoints:

### GET /horses/

Retrieves a list of all horses in the database.

<!-- #### Query Parameters

breed_type: Filters horses by breed type (e.g. Thoroughbred, Arabian, etc.)
color: Filters horses by color (e.g. black, white, etc.)
horse_type: Filters horses by type (e.g. stallion, mare, etc.)
sort: Sorts horses by the specified field (e.g. name, gen, etc.) -->

### GET /horses/:nft_id/

Retrieves a single horse by its NFT ID.

#### Request Body

* `nft_id`: The NFT ID of the horse.
* `name`: The name of the horse.
* `gen`: The genotype of the horse.
* `bloodline`: The bloodline of the horse.
* `breed_type`: The breed type of the horse.
* `horse_type`: The gender of the horse.
* `color`: The color of the horse.
* `img_url`: The URL of the horse's image.
* `parents`: An object containing the NFT IDs, names, and genders of the horse's parents.
* `offsprings`: An array of NFT IDs, names, and genders of the horse's offsprings.
* `inserted_at`: The date the horse NFT was created.
* `race_statistic`: An array of racing stats including: number of first, second, third place finishes; total races; number of free races; number of paid races; free and paid win percentages; and finishes positions by distance (1000m - 2600m).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
