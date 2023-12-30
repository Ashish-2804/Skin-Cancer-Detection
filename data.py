import joblib
data={"Melonoma":{
    "Name":"Melonoma",
    "Description":"Melanoma is a type of skin cancer that originates in melanocytes, the cells responsible for producing melanin, the pigment that gives color to the skin, hair, and eyes. It is the most serious form of skin cancer due to its potential to spread to other parts of the body. Early diagnosis and treatment are crucial for a favorable outcome. Here's an overview of the diagnosis, steps, and common symptoms of melanoma:",
    "Symptoms":["Change in Moles: Melanomas often develop within existing moles or appear as new moles. Look for changes in size, shape, color, or texture.","Irregular Borders: Melanomas often have uneven or irregular borders, unlike regular moles that tend to have smoother edges.",
                "Color Variation: Melanomas may display a mix of colors, such as shades of brown, black, blue, or even red or white.",
                "Asymmetry: Melanomas are often asymmetric, meaning one half does not match the other half in terms of appearance.",
                "Itching or Bleeding: Some melanomas may itch, bleed, or become painful."],
    "Diagonosis":["Clinical Examination: The diagnosis of melanoma often begins with a physical examination by a healthcare provider, usually a dermatologist.",
                  "Dermatoscopy: A dermatoscope, a specialized tool that allows for a closer examination of the skin, may be used to assess skin lesions and moles. This can help identify suspicious features.",
                  "Pathology Evaluation: The pathologist examines the biopsy sample under a microscope to determine if it is melanoma and, if so, its specific type and stage. "]

},
    "Actinic keratoses":{
        "Name":"Actinic keratoses",
        "Description":"Actinic keratoses, also known as solar keratoses or senile keratosis, are rough, scaly patches of skin that develop on areas of the body that are frequently exposed to the sun, such as the face, ears, neck, scalp, chest, backs of hands, forearms, or lips. These lesions are considered precancerous, as they have the potential to develop into skin cancer, typically squamous cell carcinoma. ",
        "Symptoms":["Rough, Scaly Patches: Actinic keratoses usually appear as small, dry, rough, scaly or crusty patches of skin. They may range in color from pink to reddish-brown to flesh-toned.",
                    "Itching or Burning: In some cases, these patches can be itchy or cause a burning sensation.",
                    "Enlargement: Actinic keratoses can grow over time, and in some cases, they may become raised or develop a hard, horn-like texture.",
                    "Pain: In rare instances, actinic keratoses can be tender or painful, especially when irritated."],
        "Diagonosis":["Clinical Evaluation: A dermatologist will carefully examine the affected skin and look for characteristic signs, including the appearance of rough, scaly patches in sun-exposed areas.",
                      "Dermatoscopy: Dermatoscopy, also known as dermoscopy, involves using a special magnifying lens and light source to closely examine the skin's surface, which can help in identifying specific features of the lesion.",
                      "Biopsy: In some cases, a small tissue sample (biopsy) may be taken from the affected area to confirm the diagnosis and rule out the presence of cancerous cells. There are various biopsy techniques, including shave biopsy or punch biopsy, and the choice of method may depend on the specific characteristics of the lesion."]
    },
    "Basal cell carcinoma":{
        "Name":"Basal cell carcinoma",
        "Descriptions":"Basal cell carcinoma (BCC) is a type of skin cancer that typically develops on areas of the skin exposed to the sun. Here are the common symptoms and diagnosis of basal cell carcinoma",
        "Symptoms":["A pearly or waxy bump on the skin, often with visible blood vessels.",
                    "A flat, flesh-colored or brown scar-like lesion.",
                    "A pink growth with a slightly elevated, rolled border and a crusted indentation in the center.",
                    "A sore that continuously heals and reopens.",
                    "A shiny, translucent bump or nodule, often with tiny blood vessels."],
        "Diagonosis":["Physical examination: A dermatologist will examine the affected area and evaluate the characteristics of the skin lesion.",
                      "Biopsy: A small sample of the suspicious skin tissue is taken and sent to a laboratory for analysis. This helps confirm the diagnosis and determine the subtype of basal cell carcinoma.",
                      "Imaging tests: In some cases, imaging tests like ultrasound, CT scan, or MRI may be performed to assess the extent of the cancer and determine if it has spread to nearby tissues."]
    },

        "Benign keratosis-like lesions ":
            {
                "Name":"Benign keratosis-like lesions",
                "Description":"Benign keratosis-like lesions, also known as seborrheic keratoses, are common non-cancerous skin growths that typically appear as brown, black, or tan patches on the skin. Here are the symptoms and diagnosis of benign keratosis-like lesions:",
                "Symptoms":["Raised or flat patches on the skin that may have a waxy, scaly, or rough texture.",
                            "Lesions can vary in size, ranging from small to several centimeters in diameter.",
                            "Color can range from light tan to dark brown or black.",
                            "Lesions may have a stuck-on appearance, resembling a wart or a barnacle."],
                "Diagonosis":["Visual examination: A dermatologist can usually diagnose benign keratosis-like lesions by their characteristic appearance. They will examine the skin and evaluate the size, color, texture, and shape of the lesions.",
                              "Dermoscopy: This non-invasive technique involves using a handheld device called a dermatoscope to examine the skin lesions in more detail. It helps the dermatologist differentiate between benign keratosis-like lesions and other skin conditions.",
                              "Biopsy: In some cases, a small sample of the lesion may be taken and sent to a laboratory for analysis. This is done to confirm the diagnosis and rule out any other potential skin conditions."]
            },
      "Dermatofibroma":{
          "Name":"Dermatofibroma",
          "Description":"Dermatofibroma is a common benign skin growth that usually appears as a small, firm bump on the skin. Here are the symptoms and diagnosis of dermatofibroma",
          "Symptoms":["Small, raised bump: Dermatofibromas typically present as a firm, dome-shaped or slightly raised bump on the skin.",
                      "Skin coloration: The bump may have a reddish-brown or tan color, and it often darkens with time.",
                      "Size and location: Dermatofibromas are usually small, ranging from a few millimeters to a centimeter in diameter. They commonly occur on the legs, but can also appear on other areas of the body.",
                      "Texture: The surface of a dermatofibroma may feel rough or slightly scaly. It may also dimple or become depressed when squeezed"],
          "Diagonosis":["Visual examination: A dermatologist will examine the skin lesion and evaluate its appearance, size, color, and texture. They may use a dermatoscope, a handheld device that magnifies the skin, to get a closer look.",
                        "Palpation: The dermatologist may gently press on the lesion to assess its firmness and texture.",
                        "Biopsy: In some cases, a small sample of the lesion may be taken and sent to a laboratory for analysis. This is done to confirm the diagnosis and rule out any other potential skin conditions."]
      },

}
joblib.dump(data,'data.joblib')
