import React, { useState } from 'react';
import { View, Text, Button, TextInput, Alert } from 'react-native';

const ScheduleMessageForm = () => {
    const [showForm, setShowForm] = useState(false);
    const [phoneNumber, setPhoneNumber] = useState('');
    const [name, setName] = useState('');
    const [dateTime, setDateTime] = useState('');
    const [message, setMessage] = useState('');

    const toggleForm = () => {
        setShowForm(!showForm);
    };
    
    const showMessagePopup = () => {
        Alert.alert("Your message has been scheduled");
    }

    return (
        <View>
            <Button title="Show Form" onPress={toggleForm} />

            {showForm && (
                <View>
                    <Text>Phone Number:</Text>
                    <TextInput
                        onChangeText={(text) => setPhoneNumber(text)}
                        value={phoneNumber}
                    />

                    <Text>Name:</Text>
                    <TextInput onChangeText={(text) => setName(text)} value={name} />

                    <Text>Date/Time:</Text>
                    <TextInput onChangeText={(text) => setDateTime(text)} value={dateTime} />

                    <Text>Message:</Text>
                    <TextInput onChangeText={(text) => setMessage(text)} value={message} />
                    <Button title="Schedule Message" onPress={showMessagePopup}/>
                </View>
            )}
        </View>
    );
};

export default ScheduleMessageForm;
