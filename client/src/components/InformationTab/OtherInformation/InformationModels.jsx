import {
  Accordion,
  AccordionButton,
  AccordionIcon,
  AccordionItem,
  AccordionPanel,
  Box,
  Stack,
} from "@chakra-ui/react";
import React from "react";
import { AiOutlinePlusCircle } from "react-icons/ai";
import { BiBuildings, BiTime } from "react-icons/bi";
import { CgWebsite } from "react-icons/cg";
import { MdLanguage, MdOutlineAttachMoney } from "react-icons/md";
import InformationRow from "../../InformationRow";
import When from "../../When";

export default function InformationModels({ models }) {
  return (
    <Accordion allowMultiple border="none">
      <Stack spacing={3}>
        {models.map((model) => (
          <AccordionItem border="none" key={model.name}>
            {({ isExpanded }) => (
              <>
                <AccordionButton
                  _hover={{ bg: "#f4f4f4" }}
                  _expanded={{ bg: "#f4f4f4" }}
                  borderTopRadius="xl"
                  borderBottomRadius={isExpanded ? "0" : "xl"}
                >
                  <Box
                    as="span"
                    flex="1"
                    textAlign="left"
                    color="secondary"
                    fontWeight="bold"
                    fontSize={"xl"}
                  >
                    {model.name}
                  </Box>
                  <AccordionIcon />
                </AccordionButton>
                <AccordionPanel pb={4} bg="#f4f4f4" borderBottomRadius={"xl"}>
                  <When condition={model.city}>
                    <InformationRow
                      content={model.city}
                      title="Standorte"
                      icon={BiBuildings}
                    />
                  </When>
                  <When condition={model.credit_points}>
                    <InformationRow
                      content={model.credit_points}
                      title="Leistungspunkte"
                      icon={AiOutlinePlusCircle}
                    />
                  </When>
                  <When condition={model.languages}>
                    <InformationRow
                      content={model.languages}
                      title="Unterrichtssprachen"
                      icon={MdLanguage}
                    />
                  </When>
                  <When condition={model.price}>
                    <InformationRow
                      content={model.price}
                      title="Kosten"
                      icon={MdOutlineAttachMoney}
                    />
                  </When>
                  <When condition={model.study_start}>
                    <InformationRow
                      content={model.study_start}
                      title="Studienbeginn"
                      icon={BiTime}
                    />
                  </When>
                  <When condition={model.duration}>
                    <InformationRow
                      content={model.duration}
                      title="Regelstudienzeit"
                      icon={BiTime}
                    />
                  </When>
                  <When condition={model.website_link}>
                    <InformationRow
                      content={model.website_link}
                      title="Link zur Webseite"
                      icon={CgWebsite}
                    />
                  </When>
                </AccordionPanel>
              </>
            )}
          </AccordionItem>
        ))}
      </Stack>
    </Accordion>
  );
}
