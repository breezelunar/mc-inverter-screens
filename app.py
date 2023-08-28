from flask import Flask, render_template

app = Flask(__name__)

modes = [
    {'name': 'UPS Mode', 'image': 'images/UPSMode/UPS-MODE-COVER.png', 'description': 'UPS Mode'},
    {'name': 'Solar Control Mode', 'image': 'images/SolarControlMode/SC-MODE-COVER.png', 'description': 'Solar Control Mode'},
    {'name': 'Load Shedding Mode', 'image': 'images/LoadSheddingMode/LS-MODE-COVER.png', 'description': 'Load Shedding Mode'},
]

mode_screens = {
    'UPS Mode': [
        {'id': 0, 'image': 'images/UPSMode/UPS_MainMenu/1.png', 'description': 'Inverter is on and in UPS Mode'},
        {'id': 1, 'image': 'images/UPSMode/UPS_MainMenu/2.1.png', 'description': 'Screen 2 description'},
        {'id': 2, 'image': 'images/UPSMode/UPS_MainMenu/3.1.png', 'description': 'Screen 3 description'},
        {'id': 3, 'image': 'images/UPSMode/UPS_MainMenu/4.png', 'description': 'Screen 3 description'},
        {'id': 4, 'image': 'images/UPSMode/UPS_MainMenu/5.png', 'description': 'Screen 3 description'},
        {'id': 5, 'image': 'images/UPSMode/UPS_MainMenu/6.png', 'description': 'Screen 3 description'},
        {'id': 6, 'image': 'images/UPSMode/UPS_MainMenu/7.png', 'description': 'Screen 3 description'},
        {'id': 7, 'image': 'images/UPSMode/UPS_MainMenu/8.png', 'description': 'Screen 3 description'},
        {'id': 8, 'image': 'images/UPSMode/UPS_MainMenu/9.png', 'description': 'Screen 3 description'},
    ],
    'Solar Control Mode': [
        {'id': 0, 'image': 'images/SolarControlMode/SC_MainMenu/1.png', 'description': 'Inverter is on and in UPS Mode'},
        {'id': 1, 'image': 'images/SolarControlMode/SC_MainMenu/2.1.png', 'description': 'Screen 2 description'},
        {'id': 2, 'image': 'images/SolarControlMode/SC_MainMenu/3.1.png', 'description': 'Screen 3 description'},
        {'id': 3, 'image': 'images/SolarControlMode/SC_MainMenu/4.png', 'description': 'Screen 3 description'},
        {'id': 4, 'image': 'images/SolarControlMode/SC_MainMenu/5.png', 'description': 'Screen 3 description'},
        {'id': 5, 'image': 'images/SolarControlMode/SC_MainMenu/6.png', 'description': 'Screen 3 description'},
        {'id': 6, 'image': 'images/SolarControlMode/SC_MainMenu/7.png', 'description': 'Screen 3 description'},
        {'id': 7, 'image': 'images/SolarControlMode/SC_MainMenu/8.png', 'description': 'Screen 3 description'},
        {'id': 8, 'image': 'images/SolarControlMode/SC_MainMenu/9.png', 'description': 'Screen 3 description'},
    ],
    'Load Shedding Mode': [
        {'id': 0, 'image': 'images/LoadSheddingMode/LS_MainMenu/1.png', 'description': 'Inverter is on and in UPS Mode'},
        {'id': 1, 'image': 'images/LoadSheddingMode/LS_MainMenu/2.1.png', 'description': 'Screen 2 description'},
        {'id': 2, 'image': 'images/LoadSheddingMode/LS_MainMenu/3.1.png', 'description': 'Screen 3 description'},
        {'id': 3, 'image': 'images/LoadSheddingMode/LS_MainMenu/4.png', 'description': 'Screen 3 description'},
        {'id': 4, 'image': 'images/LoadSheddingMode/LS_MainMenu/5.png', 'description': 'Screen 3 description'},
        {'id': 5, 'image': 'images/LoadSheddingMode/LS_MainMenu/6.png', 'description': 'Screen 3 description'},
        {'id': 6, 'image': 'images/LoadSheddingMode/LS_MainMenu/7.png', 'description': 'Screen 3 description'},
        {'id': 7, 'image': 'images/LoadSheddingMode/LS_MainMenu/8.png', 'description': 'Screen 3 description'},
        {'id': 8, 'image': 'images/LoadSheddingMode/LS_MainMenu/9.png', 'description': 'Screen 3 description'},
    ],
}

subset_screens = {
    'UPS Mode': {
        6: [{'image': 'images/UPSMode/UPS_SetupMenu/1.png', 'description': 'Subset Screen 1 description'},  # Subset for screen 0 in mode1
            {'image': 'images/UPSMode/UPS_SetupMenu/2.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_SetupMenu/3.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_SetupMenu/4.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_SetupMenu/5.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_SetupMenu/6.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_SetupMenu/7.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_SetupMenu/8.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_SetupMenu/9.png', 'description': 'Subset Screen 1 description'},
            ],
        7: [{'image': 'images/UPSMode/UPS_BatteryMenu/1.png', 'description': 'Subset Screen 1 description'},  # Subset for screen 0 in mode1
            {'image': 'images/UPSMode/UPS_BatteryMenu/2.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_BatteryMenu/3.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_BatteryMenu/4.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_BatteryMenu/5.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_BatteryMenu/6.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_BatteryMenu/7.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_BatteryMenu/8.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_BatteryMenu/9.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_BatteryMenu/10.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/UPSMode/UPS_BatteryMenu/11.png', 'description': 'Subset Screen 1 description'},
            ],
    },
    'Solar Control Mode': {
        6: [{'image': 'images/SolarControlMode/SC_SetupMenu/1.png', 'description': 'Subset Screen 1 description'},  # Subset for screen 0 in mode1
            {'image': 'images/SolarControlMode/SC_SetupMenu/2.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_SetupMenu/3.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_SetupMenu/4.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_SetupMenu/5.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_SetupMenu/6.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_SetupMenu/7.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_SetupMenu/8.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_SetupMenu/9.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_SetupMenu/10.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_SetupMenu/11.png', 'description': 'Subset Screen 1 description'},
            ],
        7: [{'image': 'images/SolarControlMode/SC_BatteryMenu/1.png', 'description': 'Subset Screen 1 description'},  # Subset for screen 0 in mode1
            {'image': 'images/SolarControlMode/SC_BatteryMenu/2.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_BatteryMenu/3.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_BatteryMenu/4.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_BatteryMenu/5.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_BatteryMenu/6.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_BatteryMenu/7.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_BatteryMenu/8.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_BatteryMenu/9.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_BatteryMenu/10.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/SolarControlMode/SC_BatteryMenu/11.png', 'description': 'Subset Screen 1 description'},
            ],
    },
    'Load Shedding Mode': {
        6: [{'image': 'images/LoadSheddingMode/LS_SetupMenu/1.png', 'description': 'Subset Screen 1 description'},  # Subset for screen 0 in mode1
            {'image': 'images/LoadSheddingMode/LS_SetupMenu/2.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_SetupMenu/3.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_SetupMenu/4.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_SetupMenu/5.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_SetupMenu/6.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_SetupMenu/7.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_SetupMenu/8.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_SetupMenu/9.png', 'description': 'Subset Screen 1 description'},
            ],
        7: [{'image': 'images/LoadSheddingMode/LS_BatteryMenu/1.png', 'description': 'Subset Screen 1 description'},  # Subset for screen 0 in mode1
            {'image': 'images/LoadSheddingMode/LS_BatteryMenu/2.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_BatteryMenu/3.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_BatteryMenu/4.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_BatteryMenu/5.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_BatteryMenu/6.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_BatteryMenu/7.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_BatteryMenu/8.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_BatteryMenu/9.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_BatteryMenu/10.png', 'description': 'Subset Screen 1 description'},
            {'image': 'images/LoadSheddingMode/LS_BatteryMenu/11.png', 'description': 'Subset Screen 1 description'},
            ],
    }
}

current_screen_indices = {
    'UPS Mode': 0,
    'Solar Control Mode': 0,
    'Load Shedding Mode': 0
}

@app.route('/')
def home():
    return render_template('index.html', modes=modes)

@app.route('/<mode_name>')
def show_mode_screens(mode_name):
    return render_template('mode.html', screens=mode_screens.get(mode_name, []), mode_name=mode_name, subset_screens=subset_screens)


@app.route('/<mode_name>/subset/<string:screen_id>')
def show_subset_screens(mode_name, screen_id):
    try:
        screen_id = int(screen_id)
    except ValueError:
        return "Invalid screen id", 400  # Return a 400 Bad Request error
    
    screens = subset_screens.get(mode_name, {}).get(screen_id, [])
    return render_template('subset.html', screens=screens, mode_name=mode_name)




@app.route('/currentScreenIndex/<mode_name>', methods=['GET'])
def get_current_screen_index(mode_name):
    return jsonify(screen_index=current_screen_indices.get(mode_name, 0))

@app.route('/setScreenIndex/<mode_name>/<int:screen_index>', methods=['POST'])
def set_current_screen_index(mode_name, screen_index):
    if mode_name not in current_screen_indices:
        return jsonify(success=False, message="Invalid mode_name!")
    
    current_screen_indices[mode_name] = screen_index
    return jsonify(success=True, message="Screen index updated successfully!")


if __name__ == '__main__':
    app.run(debug=True)
