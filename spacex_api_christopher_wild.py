import requests

def print_spacex_data():
    
    crew_names = []
    ship_names = []
    
    response = requests.get("https://api.spacexdata.com/v5/launches/latest")
    if response.status_code == 200:
        data = response.json()
        print('SpaceX Latest Launch Overview')
        
        #Loop over crew id's to get crew information from API
        if "crew" in data:
            for crew_id in data['crew']:
                response_crew = requests.get(f"https://api.spacexdata.com/v4/crew/{crew_id}")
                if response_crew.status_code == 200:
                    crew_names.append(response_crew.json()['name'])
            crew_names = crew_names if crew_names != [] else ['None']  #Check if not empty, if so set to list containing None
        
        #Loop over ship id's to get ship information from API    
        if "ships" in data:        
            for ship_id in data['ships']:
                response_ship = requests.get(f"https://api.spacexdata.com/v4/ships/{ship_id}")
                if response_ship.status_code == 200:
                    ship_names.append(response_ship.json()['name'])
            ship_names = ship_names if ship_names != [] else ['None'] #Check if not empty, if so set to list containing None
            
        #Get rocket information from id    
        response_rocket = requests.get(f"https://api.spacexdata.com/v4/rockets/{data['rocket']}")
        if response_rocket.status_code == 200:
            rocket_name = response_rocket.json()['name']  
            
        #Get launchpad information from id     
        response_launchpad = requests.get(f"https://api.spacexdata.com/v4/launchpads/{data['launchpad']}")
        if response_launchpad.status_code == 200:
            launchpad_name = response_launchpad.json()['name'] 
            
        print(f"Crew Members: {', '.join(crew_names)}")
        print(f"Rocket Name: {rocket_name}")
        print(f"Launchpad Site: {launchpad_name}")
        print(f"SpaceX Ships Involved In Recovery: {', '.join(ship_names)}")
    else:
        print(f'Error, could not connect to api, response: {response.status_code}')
    


    
if __name__ == '__main__':
    print_spacex_data()