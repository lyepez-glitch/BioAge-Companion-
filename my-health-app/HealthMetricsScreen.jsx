import React, { useState } from 'react';
import { View, Button, StyleSheet } from 'react-native';
import { TextInput, Text } from 'react-native-paper';  // Use TextInput and Text from react-native-paper
import { useMutation } from '@apollo/client';
import gql from 'graphql-tag';

const UPDATE_HEALTH_METRICS = gql`
  mutation UpdateHealthMetrics($restingHeartRate: Float!, $hoursOfSleep: Float!, $dailyActivityLevel: Float!) {
    updateHealthMetrics(
      restingHeartRate: $restingHeartRate
      hoursOfSleep: $hoursOfSleep
      dailyActivityLevel: $dailyActivityLevel
    ) {
      success
    }
  }
`;

export default function HealthMetricsScreen({ navigation }) {
  const [heartRate, setHeartRate] = useState('');
  const [sleepHours, setSleepHours] = useState('');
  const [activityLevel, setActivityLevel] = useState('');

  const [updateHealthMetrics, { data, loading, error }] = useMutation(UPDATE_HEALTH_METRICS);

  const handleMetricsSubmit = () => {
    updateHealthMetrics({
      variables: {
        restingHeartRate: parseFloat(heartRate),
        hoursOfSleep: parseFloat(sleepHours),
        dailyActivityLevel: parseFloat(activityLevel),
      },
    });
  };

  return (
    <View style={styles.container}>
      <Button
        style={styles.button}
        title="See Biological Age"
        color="blue"
        onPress={() => navigation.navigate('BiologicalAge')}
      />

      <TextInput
        label="Resting Heart Rate"
        value={heartRate}
        onChangeText={setHeartRate}
        keyboardType="numeric"
        style={styles.input}
        mode="outlined"
      />
      <TextInput
        label="Hours of Sleep"
        value={sleepHours}
        onChangeText={setSleepHours}
        keyboardType="numeric"
        style={styles.input}
        mode="outlined"
      />
      <TextInput
        label="Activity Level (1-10)"
        value={activityLevel}
        onChangeText={setActivityLevel}
        keyboardType="numeric"
        style={styles.input}
        mode="outlined"
      />

      <Button
        style={styles.button}
        title="Next"
        color="blue"
        onPress={handleMetricsSubmit}
      />

      {loading && <Text style={styles.loading}>Loading...</Text>}
      {error && <Text style={styles.error}>Error: {error.message}</Text>}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',  // Centers the content horizontally
    padding: 20,
  },
  input: {
    marginBottom: 15,  // Adds space below each input
    width: '70%',      // Inputs will take up 70% of the container's width
  },
  button: {
    marginTop: 15,     // Adds space above the button
    width: '70%',      // Button will take up 70% of the container's width
  },
  loading: {
    marginTop: 10,
    textAlign: 'center',
    fontSize: 16,
  },
  error: {
    marginTop: 10,
    textAlign: 'center',
    fontSize: 16,
    color: 'red',
  },
});
