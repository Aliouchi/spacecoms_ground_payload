//URL input will be of Payload OPS Ground Center
//Test Status is 200 Ok
pm.test("Status == 200", function () {
    pm.response.to.have.status(200);
});

//Verify the response has data type as valid JSON Content-type
pm.test("Content-type == JSON", function () {
    pm.response.to.have.header("Content-type", "application/json");
});


//Verify the response body has valid JSON type
pm.test("Response Body == JSON", function () {
    pm.response.to.be.json;
});


//Verify the key values present in the response
pm.test("Verify Response JSON Structure", function () {
    const expectedResponse = {
        "ID": "20231021_212435",
        "Timeframe": 500,
        "Longitude": 2.3522,
        "Latitude": 48.8566,
        "NumberOfImages": 5
    };

    const responseBody = pm.response.json();

    pm.expect(responseBody).to.eql(expectedResponse);
});


//Verify the absent keys
pm.test("Check if any unexpected key does not exist", function () {
    const expectedKeys = ["ID", "Timeframe", "Longitude", "Latitude", "NumberOfImages"];
    const responseKeys = Object.keys(pm.response.json());

    responseKeys.forEach((key) => {
        if (!expectedKeys.includes(key)) {
            pm.expect(pm.response.json()).to.not.have.key(key);
        }
    });
});

// Test for successful JSON parsing
pm.test("Successful JSON Parsing", function () {
    var validRequest = '{"ID": "20231021_212435", "Timeframe": 500, "Longitude": 2.3522, "Latitude": 48.8566, "NumberOfImages": 5}';
    var parsedData = JSON.parse(validRequest);

    pm.expect(parsedData).to.be.an('object');
    pm.expect(parsedData.ID).to.equal('20231021_212435');
    pm.expect(parsedData.Timeframe).to.equal(500);
    pm.expect(parsedData.Longitude).to.equal(2.3522);
    pm.expect(parsedData.Latitude).to.equal(48.8566);
    pm.expect(parsedData.NumberOfImages).to.equal(5);
});

// Test for handling invalid JSON
pm.test("Handling Invalid JSON", function () {
    var invalidRequest = 'This is not JSON';

    try {
        var parsedData = JSON.parse(invalidRequest);
        pm.expect(parsedData).to.be.null;
    } catch (e) {
        // If JSON parsing fails, this is expected
    }
});

// Test for missing or required fields
pm.test("Missing or Required Fields", function () {
    var incompleteRequest = '{"ID": "20231021_212435", "NumberOfImages": 5}';
    var parsedData = JSON.parse(incompleteRequest);

    // Expect the parsed data to be an object, but with some missing fields
    pm.expect(parsedData).to.be.an('object');
    pm.expect(parsedData.location).to.be.undefined;
    pm.expect(parsedData.capture_time).to.be.undefined;
});


//check acceptable response time
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

//Error handling to verify that the error structure is as expected
pm.test("Error structure is correct", function () {
    const jsonData = pm.response.json();
    if (jsonData.error) {
        pm.expect(jsonData.error).to.have.keys(['code', 'message']);
    }
});

pm.test("Verify ID Format", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson.ID).to.match(/^\d{4}\d{2}\d{2}_\d{2}\d{2}\d{2}$/);
});

pm.test("Verify Timeframe is a Number", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson.Timeframe).to.equal(500);
});

pm.test("Verify Longitude is a Number", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson.Longitude).to.equal(2.3522);
});

pm.test("Verify Latitude is a Number", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson.Latitude).to.equal(48.8566);
});

pm.test("Verify NumberOfImages is a Number", function () {
    const responseJson = pm.response.json();
    pm.expect(responseJson.NumberOfImages).to.equal(5);
});
