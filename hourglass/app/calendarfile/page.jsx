// pages/api/calendar.js

import { google } from 'googleapis';

const oauth2Client = new google.auth.OAuth2(
  "67925554077-ci50e4i28t94e9sj8jrvalu6g3lv2cp3.apps.googleusercontent.com",
  "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",
  "http://localhost:3000" + '/api/callback'
);

const fetchCalendarData = async (accessToken, refreshToken, expirationTime) => {
  oauth2Client.setCredentials({
    access_token: accessToken,
    refresh_token: refreshToken,
    scope: 'https://www.googleapis.com/auth/calendar',
    token_type: 'Bearer',
    expiry_date: expirationTime * 1000,
  });

  const calendar = google.calendar({ version: 'v3', auth: oauth2Client });

    const events = await calendar.events.list({
      calendarId: 'primary',
      timeMin: new Date().toISOString(),
      maxResults: 10,
      singleEvents: true,
      orderBy: 'startTime',
    });
    console.log(events)
    return events.data.items;
};

export default async function handler(req, res) {
    console.log(req)
    const { accessToken, refreshToken, expirationTime } = req.searchParams;
      const events = await fetchCalendarData(accessToken, refreshToken, expirationTime);

      res.status(200).json(events);
}
