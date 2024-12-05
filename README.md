<!-- write instructions to setup the virtual env with requirements.txt file and then activate it and then add key in .env.example file and then run extractor.py file -->

# Setup
1. **Create a virtual environment using the following command:**
```bash
py -m venv env
```

2. **Activate the virtual environment using the following command:**
```bash
source env/Scripts/activate
```

3. **Install the required packages using the following command:**
```bash
pip install -r requirements.txt
```

4. **Rename the `.env.example` file to `.env` file and add the API key in the `.env` file.**

5. **Run the extractor.py file using the following command:**
```bash
python extractor.py
```

6. **Deactivate the virtual environment using the following command:**
```bash 
deactivate
```

<!-- Add github url for this repo -->
**GitHub URL:** 
[amRohitKumar/text-extractor](https://github.com/amRohitKumar/text-extractor)



**NOTE**
- The image file should be in the same directory as the `extractor.py` file. The image file should be named as `image.png`.
- I've added one sample output in file named `sample_output.txt` for reference.
