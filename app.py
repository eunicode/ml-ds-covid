import flask
import pickle
import pandas as pd

# from flask import (Flask, render_template, request)

# --------------------------------------------------------------------
sex_dict = {"Male": 0, "Female": 1}

age_dict = {
    "0s": 0,
    "10s": 1,
    "20s": 2,
    "30s": 3,
    "40s": 4,
    "50s": 5,
    "60s": 6,
    "70s": 7,
    "80s": 8,
    "90s": 9,
    "100s": 10,
}

country_dict = {
    "Korea": 0,
    "China": 1,
    "United States": 2,
    "France": 3,
    "Thailand": 4,
    "Canada": 5,
    "Switzerland": 6,
    "Indonesia": 7,
    "Mongolia": 8,
    "Spain": 9,
}

province_dict = {
    "Seoul": 0,
    "Busan": 1,
    "Daegu": 2,
    "Gwangju": 3,
    "Incheon": 4,
    "Daejeon": 5,
    "Ulsan": 6,
    "Sejong": 7,
    "Gyeonggi-do": 8,
    "Gangwon-do": 9,
    "Chungcheongbuk-do": 10,
    "Chungcheongnam-do": 11,
    "Jeollabuk-do": 12,
    "Jeollanam-do": 13,
    "Gyeongsangbuk-do": 14,
    "Gyeongsangnam-do": 15,
    "Jeju-do": 16,
}

infection_source_dict = {
    "overseas inflow": 0,
    "contact with patient": 1,
    "Seongdong-gu APT": 2,
    "etc": 3,
    "Eunpyeong St. Mary's Hospital": 4,
    "Shincheonji Church": 5,
    "Dongan Church": 6,
    "Guro-gu Call Center": 7,
    "Onchun Church": 8,
    "Cheongdo Daenam Hospital": 9,
    "Suyeong-gu Kindergarten": 10,
    "Ministry of Oceans and Fisheries": 11,
    "gym facility in Cheonan": 12,
    "gym facility in Sejong": 13,
    "River of Grace Community Church": 14,
    "Gyeongsan Seorin Nursing Home": 15,
    "Gyeongsan Cham Joeun Community Center": 16,
    "Gyeongsan Jeil Silver Town": 17,
    "Bonghwa Pureun Nursing Home": 18,
    "Pilgrimage to Israel": 19,
    "Milal Shelter": 20,
    "Geochang Church": 21,
    "Changnyeong Coin Karaoke": 22,
}

# --------------------------------------------------------------------
# Load our trained model saved in a pickle file
with open(f"model/gs_logistic_regression_model_1.pkl", "rb") as f:
    model = pickle.load(f)
# rb = read binary
# loaded_model = pickle.load(open("model/gs_logistic_regression_model_1.pkl", "rb"))

# Make an app instance. `Flask` is a class
app = flask.Flask(__name__, template_folder="templates")
# __name__ is a magic variable. Use whatever the current namespace is
# `templates` - Flask automatically looks for this folder

# Homepage route
# decorator
@app.route("/", methods=["GET", "POST"])
def main():
    # If GET request, show homepage
    if flask.request.method == "GET":
        # Render
        return flask.render_template("main.html")

    # If POST request, refresh homepage
    if flask.request.method == "POST":
        # Get user input
        form_dict = flask.request.form
        # print(form_dict)

        sex = int(form_dict["sex"])
        age = int(form_dict["age"])
        country = int(form_dict["country"])
        province = int(form_dict["province"])
        infection_case = int(form_dict["infection_case"])

        # Make series to pass to model
        # input_variables = [[sex, age, country, province, infection_case]]

        # Make DataFrame to pass to model
        input_variables = pd.DataFrame(
            [[sex, age, country, province, infection_case]],
            columns=["sex", "age", "country", "province", "infection_case"],
            dtype=int,
            index=["input"],
        )

        # Call the model's predict() function
        prediction = model.predict(input_variables)[0]
        # 0 = probability the label is 0, 1 = probability the label is 1
        # print(f"Test prediction {prediction}")

        # Call the model's predict_proba() function
        prediction_prob = model.predict_proba(input_variables)[0][1]
        prediction_prob = round(prediction_prob * 100, 2)
        # prediction_prob = round((1 - prediction_prob) * 100)

        predicted_status = "low"
        if prediction_prob > 10:
            predicted_status = "high"

        # Re-render the homepage, display previous input, prediction and prediction probability
        # Pass variables
        return flask.render_template(
            "main.html",
            original_input={
                "Sex": sex,
                "Age": age,
                "Country": country,
                "Province": province,
                "Infection Case": infection_case,
            },
            result_status=predicted_status,
            result=prediction,
            result_prob=prediction_prob,
        )


if __name__ == "__main__":
    app.run(debug=True)

# =================================================================
#                             NOTES
# =================================================================
"""
https://stackoverflow.com/questions/47179348/getting-drop-down-menu-data-on-flask-via-form-is-giving-400-bad-request

--------------------------------------------------------------------
"""
