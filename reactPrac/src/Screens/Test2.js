import * as React from 'react';
import {
  Text,
  View,
  StyleSheet,
  StatusBar,
  TextInput,
  Dimensions,
  TouchableOpacity,
  ImageBackground,
  Alert,
} from 'react-native';

const windowWidth = Dimensions.get('window').width;
const statusbarHeight = StatusBar.currentHeight;
const windowHeight = Dimensions.get('window').height;
const bImage = require('./../../assets/image/background.jpg');

export default class Test2 extends React.Component {
  constructor() {
    super();
    this.state = {
      inputId: 'Enter ID',
      inputPw: 'Enter Password',
    };

    this._id = '';
    this._pw = '';
  }
  handleID = (value) => {
    this._id = value;
  };

  handlePW = (value) => {
    this._pw = value;
  };

  login = function () {
    this.setState({inputId: this._id});
    this.setState({inputPw: this._pw});

    Alert.alert('ID : ' + this.state.inputId + ' PW : ' + this.state.inputPw);
  };

  render() {
    return (
      <>
        <View style={styles.container}>
          <StatusBar translucent backgroundColor="transparent" />
          <ImageBackground source={bImage} style={styles.imageBackground}>
            <View style={styles.header}>
              <Text style={styles.headerText}>React Prac</Text>
              <Text style={styles.descText}>Todo App</Text>
            </View>

            <View style={styles.textInputContainer}>
              <TextInput
                style={styles.textInput}
                placeholder={this.state.inputId}
                placeholderTextColor="#ffffff"
                onChangeText={this.handleID}
                onSubmitEditing={this.login.bind(this)}
              />
              <TextInput
                style={styles.textInput}
                placeholder={this.state.inputPw}
                placeholderTextColor="#ffffff"
                onChangeText={this.handlePW}
              />
            </View>

            <View style={styles.footer}>
              <TouchableOpacity
                style={styles.loginButton}
                onPress={() => this.login}>
                <Text style={styles.loginButtonStyle}>Login</Text>
              </TouchableOpacity>
            </View>
          </ImageBackground>
        </View>
      </>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingTop: statusbarHeight,
  },

  imageBackground: {
    resizeMode: 'cover',
    width: windowWidth,
    height: windowHeight,
    justifyContent: 'center',
    alignItems: 'center',
  },

  header: {
    flex: 1,
  },

  headerText: {
    margin: 50,
    fontSize: 38,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#ccebd2',
  },

  descText: {
    margin: 12,
    fontSize: 20,
    textAlign: 'center',
    color: 'white',
  },

  textInputContainer: {
    flex: 1,
    margin: 7,
  },

  textInput: {
    height: 50,
    width: windowWidth,
    borderColor: '#bee0e8',
    borderWidth: 2,
    borderRadius: 30,
    margin: 7,
    textAlign: 'center',
    fontStyle: 'italic',
    fontWeight: 'bold',
    fontSize: 25,
  },

  footer: {
    flex: 1,
  },

  loginButton: {
    height: 50,
    width: 100,
    borderColor: 'white',
    borderWidth: 3,
    borderRadius: 30,
    margin: 7,
    paddingTop: 10,
  },

  loginButtonStyle: {
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#f5c895',
    fontSize: 20,
  },
});
