import * as React from 'react';
import {createBottomTabNavigator} from '@react-navigation/bottom-tabs';
import Icon from 'react-native-ionicons';
import Login from '../Screens/Login';
import Test from '../Screens/Test';
import Test2 from '../Screens/Test2';

const Tab = createBottomTabNavigator();

export default class TabNavigator extends React.Component {
  render() {
    return (
      <Tab.Navigator
        screenOptions={({route}) => ({
          tabBarIcon: ({focused}) => {
            let iconName;
            if (route.name === 'Login') {
              iconName = focused ? 'checkbox' : 'checkbox-outline';
            } else if (route.name === 'Signup') {
              iconName = focused ? 'add' : 'add';
            } else if (route.name === 'Pushup') {
              iconName = focused ? 'heart' : 'heart-empty';
            }

            return <Icon name={iconName} />;
          },
        })}
        tabBarOptions={{
          activeTintColor: 'tomato',
          inactiveTintColor: 'gray',
        }}>
        <Tab.Screen name="Login" component={Login} />
        <Tab.Screen name="Test1" component={Test} />
        <Tab.Screen name="Test2" component={Test2} />
      </Tab.Navigator>
    );
  }
}
