import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Grid";
import PersonIcon from "@mui/icons-material/Person";
import Typography from "@mui/material/Typography";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { useEffect, useState } from "react";

const Copyright = (props) => {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      fontFamily="Poppins"
      {...props}
    >
      {"Copyright © Sharad Sharma "}

      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
};

const defaultTheme = createTheme();

const SignInSide = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // Function to Handle Button Click
  const handleSubmit = async (event) => {
    event.preventDefault();

    const data = new FormData(event.currentTarget);

    // email = await data.get("email");
    // password = await data.get("password");

    console.log(JSON.stringify({ email: email, password: password }));

    // const response = await fetch("http://localhost:8000/login/result", {
    //   method: "POST",
    //   headers: { "Content-Type": "application/json" },
    // });

    const requestBody = {
      email: email,
      password: password,
    };

    const response = await fetch("http://localhost:8000/login/details", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestBody),
    });
    
  };

  return (
    <ThemeProvider theme={defaultTheme}>
      <Grid container component="main" sx={{ height: "100vh" }}>
        <CssBaseline />
        <Grid
          item
          xs={false}
          sm={4}
          md={7}
          sx={{
            backgroundImage:
              "url(https://images.unsplash.com/photo-1505764706515-aa95265c5abc?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTV8fGFncmljdWx0dXJlfGVufDB8fDB8fHww&auto=format&fit=crop&w=600&q=60)",
            backgroundRepeat: "no-repeat",
            backgroundColor: (t) =>
              t.palette.mode === "light"
                ? t.palette.grey[50]
                : t.palette.grey[900],
            backgroundSize: "cover",
            backgroundPosition: "center",
          }}
        />
        <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
          <Box
            sx={{
              my: 8,
              mx: 4,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              fontFamily: "'Poppins', sans-serif",
            }}
          >
            <Avatar sx={{ m: 1, bgcolor: "green" }}>
              <PersonIcon fontSize="large" htmlColor="#FFFFFF" />
            </Avatar>
            <Typography component="h1" variant="h5" fontFamily="Poppins">
              Sign in
            </Typography>

            {/* FORM COMPONENT */}
            <Box
              component="form"
              noValidate
              onSubmit={handleSubmit}
              sx={{ mt: 1 }}
            >
              {/* EMAIL FIELD */}
              <TextField
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                onChange={(e) => {
                  setEmail(e.target.value);
                }}
                autoFocus
                fontFamily="Poppins"
              />

              {/* PASSWORD FIELD */}
              <TextField
                margin="normal"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                onChange={(e) => {
                  setPassword(e.target.value);
                }}
                autoComplete="current-password"
                fontFamily="Poppins"
              />

              {/* REMEMBER ME CHECKBOX AND END OF FORM */}
              <FormControlLabel
                control={<Checkbox value="remember" color="primary" />}
                label="Remember me"
              />

              {/* SIGNIN BUTTON */}
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{
                  mt: 3,
                  mb: 2,
                  fontFamily: "Poppins",
                  "&:hover": {
                    border: "ActiveBorder",
                    backgroundColor: "white",
                    color: "Black",
                  },
                }}
              >
                Sign In
              </Button>

              {/* Google OAuth Button */}
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{
                  mb: 2,
                  backgroundColor: "white",
                  color: "black",
                  backgroundImage: `url(${process.env.PUBLIC_URL}/logos/google.png)`,
                  fontFamily: "Poppins",
                  backgroundSize: "20px",
                  backgroundRepeat: "no-repeat",
                  backgroundPosition: "10px center", //
                  paddingLeft: "40px",
                  "&:hover": {
                    backgroundColor: "black",
                    color: "white",
                  },
                }}
              >
                Sign In with Google
              </Button>

              {/* FORGOT PASSWORD LINK */}
              <Grid container>
                <Grid item xs>
                  <Link href="#" variant="body2" fontFamily="Poppins">
                    Forgot password?
                  </Link>
                </Grid>

                {/* DONT HAVE AN ACCOUNT LINK */}
                <Grid item>
                  <Link href="#" variant="body2" fontFamily="Poppins">
                    {"Don't have an account? Sign Up"}
                  </Link>
                </Grid>
              </Grid>

              {/* COPYRIGHT LOGO */}
              <Copyright sx={{ mt: 5 }} />
            </Box>
          </Box>
        </Grid>
      </Grid>
    </ThemeProvider>
  );
};

export default SignInSide;
