import {
  Flex,
  Stack,
  Container,
  useDisclosure,
  IconButton,
  Collapse,
  Button,
  HStack,
} from "@chakra-ui/react";
import { ReactComponent as Logo } from "../../assets/crown.svg";
import { FaTimes } from "react-icons/fa";
import { GiHamburgerMenu } from "react-icons/gi";
import MenuLinks from "./MenuLinks";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { useAuthProvider } from "../../context/authProvider";
import { Fragment } from "react";

const NavBar = ({ ...props }) => {
  const { isOpen, onToggle } = useDisclosure();
  const { pathname } = useLocation();
  const navigate = useNavigate();
  const { remove } = useAuthProvider();
  const pathnames = ["/register", "/login", "/activate"];

  const logout = () => {
    remove();
    localStorage.removeItem("token");
    navigate("/login");
  };

  if (!pathnames.includes(pathname)) {
    return (
      <Fragment key={Math.random()}>
        <Flex
          boxShadow={"lg"}
          as="nav"
          p={4}
          mb={{ base: 0, md: 8 }}
          bg={"white"}
          color={"black"}
          position="fixed"
          width="100%"
          zIndex={2}
          {...props}
        >
          <Container
            maxW="8xl"
            display={"flex"}
            justifyContent="space-between"
            alignItems="center"
            wrap="wrap"
          >
            <Link to="/">
              <Logo />
            </Link>
            <IconButton
              onClick={onToggle}
              icon={
                isOpen ? (
                  <FaTimes w={3} h={3} />
                ) : (
                  <GiHamburgerMenu w={5} h={5} />
                )
              }
              variant={"ghost"}
              aria-label={"Toggle Navigation"}
              display={{ base: "flex", md: "none" }}
            />
            {!localStorage.getItem("token") ? (
              <Stack
                spacing={8}
                align="center"
                justify={["center", "space-between", "flex-end", "flex-end"]}
                direction={["column", "row", "row", "row"]}
                pt={[4, 4, 0, 0]}
                display={{ base: "none", md: "flex" }}
              >
                <MenuLinks />
              </Stack>
            ) : (
              <HStack>
                <Link to="/bookmarks">
                  <Button variant={"primary"}>Bookmarks</Button>
                </Link>
                <Button onClick={logout} variant={"ghost"}>
                  Logout
                </Button>
              </HStack>
            )}
          </Container>
        </Flex>
        <Collapse in={isOpen} animateOpacity>
          <MobileNav />
        </Collapse>
      </Fragment>
    );
  }
};

export default NavBar;

const MobileNav = () => {
  return (
    <Stack p={4} display={{ md: "none" }} bg="secondary" mt="16" zIndex={2}>
      <MenuLinks />
    </Stack>
  );
};
