import { Box, Container, Stack, Link } from "@chakra-ui/react";
import { useLocation } from "react-router-dom";

const Footer = () => {
  const { pathname } = useLocation();
  const pathnames = ["/register", "/login", "/activate"];

  if (!pathnames.includes(pathname)) {
    return (
      <Box
        bg="black"
        left={0}
        right={0}
        bottom={0}
        position="sticky"
        top="100%"
      >
        <Container
          as={Stack}
          maxW={"6xl"}
          py={4}
          direction={{ base: "column", md: "row" }}
          spacing={4}
          justify={{ base: "center", md: "space-between" }}
          align={{ base: "center", md: "center" }}
          color={"white"}
          w="100%"
        >
          <Stack direction={"row"} spacing={6} ml="auto" mr="0">
            <Link href={"/contact"}>Kontakt</Link>
            <Link href={"/license"}>Lizenz</Link>
            <Link href={"/impressum"}>Impressum</Link>
          </Stack>
        </Container>
      </Box>
    );
  }
};

export default Footer;
