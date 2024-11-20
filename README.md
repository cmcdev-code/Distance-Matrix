# Instructions to Run

1. **Navigate to the directory containing the `DistanceMatrix.py` file.**

2. **Install the required packages by running:**

   ```sh
   pip install -r requirements.txt
   ```

   *This will install the external pip packages needed for the project:*

   - **`requests`** to access the API
   - **`pandas`** for data manipulation
   - **`PyYAML`** for project configuration

   *Note: You may need to replace `pip` with `pip3`.*

3. **Edit the configuration file:**

   - Open the `config.yaml` file.
   - Update the `api_key` with your own API key (ensure it is enclosed in quotation marks).
   - Set `inputFile` to your data input file.
   - Specify `outputDistFile` and `outputTimeFile` with your desired output file names.

4. **Run the script:**

   - Click the "play" button at the top right of the screen, **or**
   - Execute the following command:

     ```sh
     python DistanceMatrix.py
     ```