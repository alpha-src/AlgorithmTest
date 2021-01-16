import * as React from 'react';
import {Button, Text, View} from 'react-native';
import {createStackNavigator} from '@react-navigation/stack';

function LoginScreen({navigation}) {
  return (
    <View style={{justifyContent: 'center', flex: 1}}>
      <Text>Login</Text>
      <Button
        title="Login Button"
        onPress={() => navigation.navigate('Home')}></Button>
    </View>
  );
}

const LoginStack = createStackNavigator();

export default function LoginStackScreen() {
  return (
    <LoginStack.Navigator>
      <LoginStack.Screen name="Login" component={LoginScreen} />
    </LoginStack.Navigator>
  );
}
